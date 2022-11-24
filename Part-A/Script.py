from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from urllib3 import exceptions
from tqdm import tqdm
from time import time as Time
import pandas as pd
from openpyxl import workbook
from numpy.random import randint

import time
import unittest
import json
import requests
import urllib3


def calc_time(link):
    milliseconds = int(Time() * 1000)
    driver2.get(link)
    milliseconds2 = int(Time() * 1000)
    time1 = (milliseconds2-milliseconds)/float(1000)
    link_times.add((link, time1))


option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
with webdriver.Chrome(options=option) as driver:
    driver.minimize_window()
    print("\n")

    website = ''
    ttl = 0
    wname = ''
    while website == '':
        srno = 1
        srno = int(input("Enter the SrNo. of the link you want to crawl:\n\n1) https://nrega.nic.in/Nregahome/MGNREGA_new/Nrega_home.aspx\n2) https://www.usa.gov/\n3) https://www.bits-pilani.ac.in/\n4) https://www.isro.gov.in/\n5) https://medium.com/\n6) https://www.education.gov.in/en\n\n"))
        if srno == 1:
            website = 'https://nrega.nic.in/Nregahome/MGNREGA_new/Nrega_home.aspx'
            wname = "NREGA"
            ttl = 141
        elif srno == 2:
            website = 'https://www.usa.gov/'
            wname = "USA"
            ttl = 226
        elif srno == 3:
            website = 'https://www.bits-pilani.ac.in/'
            wname = "BITS"
            ttl = 104
        elif srno == 4:
            website = 'https://www.isro.gov.in/'
            wname = "ISRO"
            ttl = 156
        elif srno == 5:
            website = 'https://medium.com/'
            wname = "MEDIUM"
            ttl = 86
        elif srno == 6:
            website = 'https://www.education.gov.in/en'
            wname = "EDU"
            ttl = 306
        else:
            print("\nInvalid input, try again.\n")

    print("\nNow crawling : %s....\n" % website)

    ctr = 0

    pbar = tqdm(total=ttl)

    driver.get(website)
    time.sleep(1)

    hlinks = {1}
    harea = {1}
    hblockquotes = {1}
    himg = {1}

    base_url = website

    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        ins = len(hlinks)
        hyperlink = link.get_attribute("href")
        if hyperlink == None:
            continue
        if hyperlink.startswith('javascript'):
            continue
        if not (hyperlink.startswith("http")):
            hyperlink = base_url + hyperlink
        hlinks.add(hyperlink)
        fs = len(hlinks)
        if ins != fs:
            pbar.update(1)

    hlinks.remove(1)

    # print("\nAnchor links:\n")
    # for link in hlinks:
    #     print("%s"%link)

    links = driver.find_elements(By.TAG_NAME, "area")
    for link in links:
        ins = len(harea)
        hyperlink = link.get_attribute("href")
        if hyperlink == None:
            continue
        if hyperlink.startswith('javascript'):
            continue
        if not (hyperlink.startswith("http")):
            hyperlink = base_url + hyperlink
        harea.add(hyperlink)
        fs = len(harea)
        if ins != fs:
            pbar.update(1)

    harea.remove(1)

    # print("\nArea links:\n")
    # for link in harea:
    #     print("%s"%link)

    links = driver.find_elements(By.TAG_NAME, "blockquote")
    for link in links:
        ins = len(hblockquotes)
        hyperlink = link.get_attribute("cite")
        if hyperlink == None:
            continue
        if hyperlink.startswith('javascript'):
            continue
        if not (hyperlink.startswith("http")):
            hyperlink = base_url + hyperlink
        hblockquotes.add(hyperlink)
        fs = len(hblockquotes)
        if ins != fs:
            pbar.update(1)
    links = driver.find_elements(By.TAG_NAME, 'del')
    for link in links:
        ins = len(hblockquotes)
        hyperlink = link.get_attribute("cite")
        if hyperlink == None:
            continue
        if hyperlink.startswith('javascript'):
            continue
        if not (hyperlink.startswith("http")):
            hyperlink = base_url + hyperlink
        hblockquotes.add(hyperlink)
        fs = len(hblockquotes)
        if ins != fs:
            pbar.update(1)
    links = driver.find_elements(By.TAG_NAME, 'ins')
    for link in links:
        ins = len(hblockquotes)
        hyperlink = link.get_attribute("cite")
        if hyperlink == None:
            continue
        if hyperlink.startswith('javascript'):
            continue
        if not (hyperlink.startswith("http")):
            hyperlink = base_url + hyperlink
        hblockquotes.add(hyperlink)
        fs = len(hblockquotes)
        if ins != fs:
            pbar.update(1)
    links = driver.find_elements(By.TAG_NAME, 'q')
    for link in links:
        ins = len(hblockquotes)
        hyperlink = link.get_attribute("cite")
        if hyperlink == None:
            continue
        if hyperlink.startswith('javascript'):
            continue
        if not (hyperlink.startswith("http")):
            hyperlink = base_url + hyperlink
        hblockquotes.add(hyperlink)
        fs = len(hblockquotes)
        if ins != fs:
            pbar.update(1)

    hblockquotes.remove(1)

    # print("\nBlockquotes links:\n")
    # for link in hblockquotes:
    #     print("%s"%link)

    links = driver.find_elements(By.TAG_NAME, "img")
    for link in links:
        ins = len(himg)
        hyperlink = link.get_attribute("longdesc")
        if hyperlink == None:
            continue
        if hyperlink.startswith('javascript'):
            continue
        if not (hyperlink.startswith("http")):
            hyperlink = base_url + hyperlink
        himg.add(hyperlink)
        fs = len(himg)
        if ins != fs:
            pbar.update(1)

    himg.remove(1)

    # print("\nImage links:\n")
    # for link in himg:
    #     print("%s"%link)

    pbar.close()

    print("\n\nTotal anchor links : %d" % len(hlinks))
    print("Total area links : %d" % len(harea))
    print("Total blockquote links : %d" % len(hblockquotes))
    print("Total image links : %d\n" % len(himg))

    All_Links = hlinks.union(harea, hblockquotes, himg)

    print("\nProcessing links :\n")
    with webdriver.Chrome(options=option) as driver2:
        driver2.minimize_window()
        pbar1 = tqdm(total=len(All_Links))
        dead_links = {("hello", 1)}
        link_times = {("hello", float(1))}
        for link in All_Links:
            # print("Link number : %d"%count)
            # print("Link : %s"%link)
            try:
                request = requests.head(link, verify=False)
                status_code = request.status_code
                if status_code >= 400:
                    # print("******* ")
                    dead_links.add((link, status_code))
                else:
                    calc_time(link=link)
                # print("Status code : %d\n"%status_code)
            except Exception as e:
                #print("Error while checking the link status \n%s"%str(e))
                dead_links.add((link, 400))
            pbar1.update(1)

        pbar1.close()

        print("\nVerifying dead links :\n")

        dead_links.remove(("hello", 1))
        link_times.remove(("hello", 1))

        pbar2 = tqdm(total=len(dead_links))

        itrc = 1
        ins = len(dead_links)
        fs = 0

        # print("\n*********************************\niteration: %d\n"%itrc)

        count = 0
        dl1 = {("Hello", 1)}
        al1 = {"hello"}
        for link in dead_links:
            count += 1
            # print("Link number : %d"%count)
            # print("Link : %s"%link[0])
            try:
                request = requests.head(link[0], verify=False)
                status_code = request.status_code
                if status_code >= 400:
                    request = requests.get(link[0], verify=False)
                    status_code = request.status_code
                    if status_code >= 400:
                        request = requests.put(link[0], verify=False)
                        status_code = request.status_code
                        if status_code >= 400:
                            request = requests.post(link[0], verify=False)
                            status_code = request.status_code
                            if status_code >= 400:
                                request = requests.patch(link[0], verify=False)
                                status_code = request.status_code
                                if status_code >= 400:
                                    # print("******* ")
                                    dl1.add((link[0], status_code))
                                    # print("Status code : %d\n"%status_code)
                                else:
                                    calc_time(link=link[0])
                            else:
                                calc_time(link=link[0])
                        else:
                            calc_time(link=link[0])
                    else:
                        calc_time(link=link[0])
                else:
                    calc_time(link=link[0])
            except Exception as e:
                # print("Error while checking the link status \n%s"%str(e))
                dl1.add((link[0], 400))
            pbar2.update(1)

        itrc += 1

        dl1.remove(("Hello", 1))
        dead_links = dl1
        fs = len(dead_links)
        dc = ins-fs
        # print("invalid deadlinks removed = %d"%dc)

        while ins != fs:
            ins = len(dead_links)
            pbar2.reset(ins)
            # print("\n*********************************\niteration: %d\n"%itrc)

            count = 0
            dl1 = {("Hello", 1)}
            for link in dead_links:
                count += 1
                # print("Link number : %d"%count)
                # print("Link : %s"%link[0])
                try:
                    request = requests.head(link[0], verify=False)
                    status_code = request.status_code
                    if status_code >= 400:
                        request = requests.get(link[0], verify=False)
                        status_code = request.status_code
                        if status_code >= 400:
                            request = requests.put(link[0], verify=False)
                            status_code = request.status_code
                            if status_code >= 400:
                                request = requests.post(link[0], verify=False)
                                status_code = request.status_code
                                if status_code >= 400:
                                    request = requests.patch(
                                        link[0], verify=False)
                                    status_code = request.status_code
                                    if status_code >= 400:
                                        # print("******* ")
                                        dl1.add((link[0], status_code))
                                        # print("Status code : %d\n"%status_code)
                                    else:
                                        calc_time(link=link[0])
                                else:
                                    calc_time(link=link[0])
                            else:
                                calc_time(link=link[0])
                        else:
                            calc_time(link=link[0])
                    else:
                        calc_time(link=link[0])
                except Exception as e:
                    # print("Error while checking the link status \n%s"%str(e))
                    dl1.add((link[0], 400))
                pbar2.update(1)

            itrc += 1

            dl1.remove(("Hello", 1))
            dead_links = dl1
            fs = len(dead_links)
            dc = ins-fs
            # print("invalid deadlinks removed = %d"%dc)
        pbar2.close()

        print("\n\n\nNumber of dead links : %d\n" % len(dead_links))
        for link in dead_links:
            print(link[0])
        avtime = float(0)
        # print("\n\n\nNumber of active links : %d\n"%len(link_times))
        for link in link_times:
            # print(link[0]+" "+str(link[1]))
            avtime += link[1]

        avtime = avtime/float(len(link_times))

        print("\n\nAverage time : %f" % avtime)

        for link in dead_links:
            x = link[0]
            y = -1
            link_times.add((x, y))

        print("\n")

        inx = 1
        link1 = next(iter(link_times))
        link_times.remove(link1)
        list1 = pd.DataFrame({'Website': {inx: website}, 'Link': {
                             inx: link1[0]}, 'Time': {inx: link1[1]}, 'Alive': {inx: 'Y'}})
        for link in link_times:
            a = link[0]
            b = link[1]
            if b != -1:
                list1.loc[len(list1.index)+1] = [website, a, b, 'Y']
            else:
                list1.loc[len(list1.index)+1] = [website, a, '-', 'N']
        file = wname+'.xlsx'
        list1.to_excel(file)

        driver2.close()
        driver.close()
