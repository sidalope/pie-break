#!/usr/bin/env python3

import time
import webbrowser
from sys import argv, exit
import random


class PieBreak:
    """A timer class which accepts custom work times and listas of urls"""

    def __init__(
        self, work_time=70,
        urls=['https://en.wikipedia.org/wiki/Special:Random']
    ):
        self.work_time = work_time
        if urls:
            self.urls = urls

    def get_params(self):
        return self.work_time, self.urls

    def get_random_url(self):
        """Return a random url at random from urls.txt or default"""

        if len(self.urls) > 1:
            print(urls)
            return random.choice(urls)
        else:
            try:
                with open('urls.txt', 'r') as links_file:
                    links = links_file.readlines()
                    links = [link.rstrip("\n") for link in links]
            except FileNotFoundError:
                # If no file is present return the default url
                print('urls.txt file not found. Using defaults...')
                return self.urls[0]
            else:
                # if the file could be found and parsed, return a url at random
                print('Reading urls from file..')
                if len(links) > 0:
                    return random.choice(links)

    def run(self):
        """Repeatedly open a url after a user-specified number of minutes"""

        print(f'\r\nWorking for {self.work_time} minutes')
        count = 0
        while True:
            url = self.get_random_url()
            print(f'Distraction URL is: {url}\r\n')
            time.sleep(int(self.work_time) * 60)
            # TODO print time
            print(
                f'Break {count}: {self.work_time} minutes have \
                  passed. Time for a break.'
            )
            count += 1
            webbrowser.open(url)


if __name__ == '__main__':
    """If multiple arguments are passed, parse the first as
    "working minutes" and the rest as urls"""

    timer = None

    # If a time and several urls are passed
    if len(argv) >= 3:
        try:
            timer = PieBreak(work_time=int(argv[1]), urls=argv[2:])
        except ValueError:
            work_time = input(
                'Try again. For how many minutes do you want to work? ')
            try:
                work_time = int(work_time)
            except ValueError:
                exit(
                    'You use numbers like elon musk names children.. Exiting.')
            else:
                urls = []
                while True:
                    if urls:
                        new_url = input('Another?: ')
                    else:
                        new_url = input(
                            'If you want, enter a url by which to be \
                                interrupted: ')
                    if not new_url:
                        break
                    urls.append(new_url)

                timer = PieBreak(work_time=work_time, urls=urls)
        timer.get_params()

    # If only a working time is passed
    elif len(argv) == 2:
        try:
            timer = PieBreak(work_time=int(argv[1]))
        except ValueError:
            work_time = input(
                'Try again. For how many minutes do you want to work?')

    # If no parameters are passed
    else:
        timer = PieBreak()

    print(timer.get_params())
    timer.run()
