*****************   文件说明 **********************
dem_file: 以txt格式存储爬取的dem文件url信息。
download：存储下载dem的文件夹


***************** 需要的库  ***************
1.安装wget：https://eternallybored.org/misc/wget/
选择64-bit exe文件下载，并复制到C:/windows/system32文件夹下

2.安装requests库： pip install requests



*****************   操作说明   *********************
1.获取所选区域dem文件的下载url信息
打开process.py文件，根据import后的结果修改POLYGON数据值
在"cmd"中切换至source文件夹，执行（以下载E49区数据为例），得到url信息文件存至dem_file：
python process.py  --region_name E49

2.下载选中区域的dem文件，至download文件夹
python download.py --region_name E49
