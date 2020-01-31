import sys
import requests
import lxml.html
from urllib.request import urlopen
from operator import eq

from bs4 import BeautifulSoup
from multiprocessing import Pool
import time

# r = requests.get('http://hanbit.co.kr')
# print(r.json)
# tree = lxml.html.parse('full_book_list.html')


def test1():
    tree = lxml.html.parse(urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html'))
    # print(type(tree))
    html = tree.getroot()
    # print(type(html))

    # print(html.cssselect('li'))
    h1 = html.xpath('//h1')[0]
    print(h1.attrib)


def extraction_num(arrage_num):
    prize_number = []

    # my_titles는 list 객체
    for num in arrage_num:
        # Tag안의 텍스트
        prize_number.append(num.text)

    return prize_number


def get_looto_num(num):
    numList = []
    req = requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo='+num)
    #http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=[NUM]


    # HTML 소스 가져오기
    html = req.text
    '''
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok
    '''
    if req.ok == False or req.status_code != 200:
        print('error')
        return 'error'
    # sys.exit()
    soup = BeautifulSoup(html, 'html.parser')
    # article > div:nth-child(2) > div > div.win_result > h4 > strong
    round = soup.select('#article > div:nth-child(2) > div > div.win_result > h4 > strong')
    # print(round[0].text)
    # sys.exit()
    if eq(round[0].text, '회'):
    # if '회' in my_titles[0].text:
        print('end')
        return 'end'

    #article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball1
    #article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball2
    #article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball3
    #article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball4
    #article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball5
    #article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span
    digit_one = soup.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball1')
    digit_ten = soup.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball2')
    digit_2ten = soup.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball3')
    digit_3ten = soup.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball4')
    digit_4ten = soup.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball5')
    digit_bonus = soup.select('#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span')
    numList += (extraction_num(digit_one))
    numList += (extraction_num(digit_ten))
    numList += (extraction_num(digit_2ten))
    numList += (extraction_num(digit_3ten))
    numList += (extraction_num(digit_4ten))
    # numList.sort()
    numList.append(extraction_num(digit_bonus))

    return numList


def looto_process(n):
    lotto_num_list = {}

    res = get_looto_num(str(n))

    if eq(res, 'end') or eq(res, 'error'):
        return lotto_num_list;
    # print(res)
    lotto_num_list = {
        'round_id': n,
        'game': res
    }

    return lotto_num_list


def getStartLotto(endRound = 889):
    lotto_num_list = {}
    pool = Pool(5) # n개의 프로세스를 사용합니다.
    lotto_num_list = pool.map(looto_process, range(1, int(endRound)+1)) # pool에 일을 던져줍니다.
    # print(lotto_num_list)
    return lotto_num_list


if __name__ == '__main__':
    getStartLotto()
    exit()

'''

round = 877
while True:
    res = get_looto_num(str(round))

    if eq(res,'end') or eq(res,'error'):
        break;
    lotto_num_list[round] = res
    print(res)
    round += 1
'''

