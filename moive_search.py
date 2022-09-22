# -*- coding: utf-8 -*-

# 电影搜索脚本，可搜索国内各大网盘资源
# 使用到的第三方库：requests，lxml
# 本程序使用网盘搜磁力蜘蛛的搜索结果
# 经由程序搜索所产生的任何结果皆不代表本人立场
# 本人不对其真实合法性以及版权负责，亦不承担任何法律责任
# 使用方法：终端中输入 “python moive_search.py”运行
# Author：Taylor
# Email：tianming_mail2022@yet.net
# Version：1.0

import requests
from lxml import etree

cilizhizhu_url = "http://www.btmovi.cool/"
count = 1


def search(keywords, start_page=1, end_page=1):
    global count
    current_page = start_page
    while current_page <= end_page:
        search_url = cilizhizhu_url + 'so/' + ','.join(keywords) + '_' + 'rel' + '_' + str(current_page) + '.html'
        r = requests.get(search_url)
        tree = etree.HTML(r.content)
        result_list = tree.xpath("//div[@class='item-title']/h3/a")

        if len(result_list) == 0:
            print("*********************************************")
            print("对不起，这个真没有！")
            print("虽然已经很努力了，但还是没能找到您想要的结果。")
            print("*********************************************", '\n')

        url_and_content_list = []
        for result in result_list:
            tmp_name_url = []
            tmp_name = result.xpath("./text()")
            tmp_url = result.xpath("./@href")
            tmp_name_url.append(' '.join(tmp_name))
            tmp_name_url.append(cilizhizhu_url.rsplit('/', 1)[0] + tmp_url[0])

            url_and_content_list.append(tmp_name_url)

        for item in url_and_content_list:
            print('{}({})'.format(item[0], item[1]))

        current_page = current_page + 1


def main():
    print('''
            #########################################################
            # 电影搜索脚本，可搜索国内各大网盘资源
            # 使用到的第三方库：requests，lxml
            # 本程序使用网盘搜磁力蜘蛛的搜索结果
            # 经由程序搜索所产生的任何结果皆不代表本人立场
            # 本人不对其真实合法性以及版权负责，亦不承担任何法律责任
            # 使用方法：终端中输入 “python moive_search.py”运行
            # Author：Taylor
            # Email：tianming_mail2022@yet.net
            # Version：1.0
            #########################################################''')

    while True:
        kw = input("请输入影片名字（多个关键字请以空格隔开）:")
        keywords = kw.split(' ')
        page = input("请输入要查找的结果显示页数:0代表结束搜索：")
        if not page.isalnum():
            print("请输入一个整数！")
            continue
        if int(page) == 0:
            break
        search(keywords, end_page=int(page))


if __name__ == '__main__':
    main()
