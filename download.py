import wget
import subprocess
import os

import argparse				#导入区域名



if __name__ == '__main__':

    parser = argparse.ArgumentParser()	
    parser.add_argument('--region_name', type=str, default="download")
    args = parser.parse_args()
    region_name = args.region_name
    dem_path = "dem_file/"+region_name+"_url.txt"
    download_path = "download/"+region_name

    with open(dem_path, 'r', encoding='utf-8') as f:
        url = [i[:-1].split('\n') for i in f.readlines()]

    for url_link in url:
        file_name = wget.filename_from_url(url_link[0])
        out = download_path+file_name
        cmd='wget -O %s %s --http-user=w_h163.com  --http-passwd=Wh123456' % (out,url_link[0])
        #subprocess.call(cmd,shell=True)  #for Linux
        os.system(cmd)                    #for Win
