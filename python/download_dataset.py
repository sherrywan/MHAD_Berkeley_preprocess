'''
Author: wxy
Date: 2023-03-07 19:45:03
LastEditors: wxy
LastEditTime: 2023-03-07 21:23:14
Description: 
FilePath: \data_preprocess\download_dataset.py
'''
import requests
import gdown
import os


def download_file_from_google_drive(destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://doc-b8-78-drive-data-export.googleusercontent.com/download/s8tg3ro1etjqrpgtvjen87q6e41b8mm7/kemjve86mm830makh6damsdndgj707ff/1678176000000/59263279-79e7-4029-807b-0953a77ede85/118283618185489056066/ADt3v-McxRAIUbw9o3GG0zbUwzzjmBWmDYsKDylVGv32H8UOAD03a1rXhvnbOil7_nismB8RfRPTp7maGrz1Nkxe9EA8pvzA-MEbi403g_p3i6Tfy_gyyYuNsSpbdDDvsxV7rCIE8WtRN3_gSikKSQJ64zNGmEdQsseceQcnsKpNJa06fxxJlfF5WuX167YxpW3WTgmlz_eHRWceKGjTaVzWklUf6A_p0ZYV-W1shS9KYHKkLa4RiUPT8Um2zHQm9sIrpH0h6DbMcH4Y5xsMH1MDu86KqmFFolqbxJmuMdEVhClgAQbCFs79qHdF4diSmWCpi7-1TIzL?nonce=m9bnhv33eapt2&user=118283618185489056066&authuser=0&hash=mffhp61fkk2ejb45hr88nh4co8e878ar"

    session = requests.Session()

    response = session.get(URL, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


def down_by_gdown(url, drc, fuzzy=False):
    if fuzzy:
        gdown.download(url=url, output=drc, quiet=False, fuzzy=True)
    else:
        gdown.download_folder(url, output=drc, quiet=True, use_cookies=False, remaining_ok=True)

if __name__ == "__main__":
    cam_dic = {1:"https://drive.google.com/drive/folders/1hdqgr1Q2B6FLb0LM0Zwm8epMD9X1geVs?usp=sharing",
                2:"https://drive.google.com/drive/folders/1ghXfYrLsx_y4ie47ZoUgF1D4vlfvQVQN?usp=sharing",
                3:"https://drive.google.com/drive/folders/12O04N7EatBmUz0kIosWfLlvLWWFmEkFK?usp=sharing",
                4:"https://drive.google.com/drive/folders/1ibFQQ-fqVwUPdHFej0ydoJHmyIeV_zlK?usp=sharing"}
    drc = "D:/dataset/MHAD/raw_data/Camera/Cluster01"
    for cam, url in cam_dic.items():
        print("start download cam%d dataset"%cam)
        drc_folder = os.path.join(drc, "Cam%02d"%cam)
        down_by_gdown(url, drc, fuzzy=False)
    