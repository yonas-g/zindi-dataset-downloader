class ZindiDataDownloader:
  def __init__(self, auth_token):
    self.auth_token = auth_token

    
  def fetch(self, url, target_name = None, target_path='./'):
    '''
    Load and extract the given url dataset
    '''
    import requests
    import requests, zipfile
    import os
    from functools import partial
    from tqdm import tqdm
    tqdm = partial(tqdm, position=0, leave=True)

    auth_obj = {
        'auth_token': self.auth_token
    }

    response = requests.post(url, data = auth_obj, stream=True)

    file_name = target_name if target_name != None  else url[url.rindex('/'): ]
    file_path = target_path + file_name

    handle = open(file_path, "wb")

    total_size_in_bytes= int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
            progress_bar.update(len(chunk))
            handle.write(chunk)

    handle.close()
    progress_bar.close()

    # if needs extraction
    compress_file_types = ['zip', '7z', 'bz2', 'gz', 'rar', 'tar']

    if file_path[file_path.rindex('.')+1:] in compress_file_types:
      from zipfile import ZipFile
      with ZipFile(file_path, 'r') as zipObj:
        zipObj.extractall(target_path)

    print(file_name, 'downloading and extracting finished')
