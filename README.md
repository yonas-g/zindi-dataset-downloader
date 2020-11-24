# Download Datasets from Zindi!

```python
import ZindiDownloader as zindi

# this can be found by inspecting html element of dataset's webpage. CTRL + f
url = 'https://api.zindi.africa/v1/competitions/sbtic-animal-classification/files/train_zebras.zip'

auth_token = '1234' # this can be found by inspecting html element of dataset's webpage. CTRL + f and  searh for 'auth'

downloader = zindi(auth_token)

downloader.fetch(url, target_path='./')

```

