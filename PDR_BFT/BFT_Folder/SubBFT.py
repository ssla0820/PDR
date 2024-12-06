import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir)))

from PDR.pages import base_page
from PDR.ATFramework.Framework1 import Framework1
from PDR.ATFramework.Framework2 import Framework2


def main():
    pages = base_page.basePage('subBFT')
    Framework1Page = Framework1.Framework1Page('subBFT')
    Framework2Page = Framework2.Framework2Page('subBFT')

    pages.data()
    Framework1Page.data()
    Framework2Page.data()