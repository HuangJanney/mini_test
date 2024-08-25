from page.main_page import MainPage
from utils.log_util import logger
from airtest.core.api import *
from airtest.aircv import *



class PatryPage(MainPage):


    #点击派对icon，打开派对界面
    def patry_mian(self):
        if self.exists_recursively_default('main_ui','party_icon.png'):
            self.touch_recursively_default('main_ui','party_icon.png')
            #验证是否开启
            if self.exists_recursively_default('main_ui','create_party.png'):
                logger.info('已打开派对界面')
            elif self.exists_recursively_default('main_ui','party_icon.png'):
                self.touch_coordinate(0.838, 0.397)#通过相对坐标点击，建议使用1080*2040分辨率的
                if self.exists_recursively_default('main_ui','create_party.png'):
                    logger.info('已打开派对界面')

    #创建派对
    def create_party(self,patry_type:int=0):
        """    
        :param party_type= 0:chat 1:fashion 2:game 3:fireworks 4:birthday 5:music
        """
        if self.exists_recursively_default('main_ui','create_party.png'):
            self.touch_recursively_default('main_ui','create_party.png')
            #开启后进行派对选择
            if self.exists_recursively_default('main_ui','hold_icon.png'):
                patry_type_list = ['chat_party.png','fashion_patry.png','game_party.png','fireworks_patry.png','birthday_party.png','music_party.png']
                self.touch_recursively_default('main_ui',patry_type_list[patry_type])
                sleep()
                self.touch_recursively_default('main_ui','hold_icon.png')
                #判断是否点击生效
                if not self.exists_recursively_default('main_ui','hold_icon.png'):
                    logger.info('派对创建中')
                    self.sleep(5)
                    wait_time = 0
                    while wait_time < 20:
                        try:
                            flag = bool(self.exists_recursively_default('main_ui','hand_icon.png'))
                            flag_close = bool(self.exists_recursively_default('main_ui','close_party.png'))
                            logger.info(flag)
                            if self.exists_recursively_default('main_ui','tips.png'):
                                self.error_report()
                                break
                            elif flag == False and flag_close == False:
                                self.sleep(1)
                                logger.info("派对创建中，请等待...")
                            elif self.exists_recursively_default('rookie_guide','next_page.png'):#首次开启派对界面引导处理
                                while True:
                                    if self.exists_recursively_default('rookie_guide','next_page.png'):
                                        self.touch_recursively_default('rookie_guide','next_page.png')
                                    elif self.exists_recursively_default('rookie_guide','close_page.png'):
                                        self.touch_recursively_default('rookie_guide','close_page.png')
                                        break
                            # elif flag == True or flag_sign == True:
                            elif flag  or flag_close :
                                logger.info('派对创建完成')
                                break
                        except:
                            logger.info('派对创建异常')
                        wait_time += 1              


    #关闭派对
    def close_party(self):
        if self.exists_recursively_default('main_ui','close_party.png'):
            self.touch_recursively_default('main_ui','close_party.png')
            if self.exists_recursively_default('main_ui','confirm_icon.png'):
                self.touch_recursively_default('main_ui','confirm_icon.png')
                #判断是否离开派对
                if not self.exists_recursively_default('main_ui','confirm_icon.png'):
                    logger.info('离开派对中')
                    self.sleep(5)
                    wait_time = 0
                    while wait_time < 20:
                        try:
                            flag = bool(self.exists_recursively_default('main_ui','hand_icon.png'))
                            flag_close = bool(self.exists_recursively_default('main_ui','close_party.png'))
                            logger.info(flag)
                            if self.exists_recursively_default('main_ui','tips.png'):
                                self.error_report()
                                break
                            elif flag == False and flag_close == False:
                                self.sleep(1)
                                logger.info("离开派对，请等待...")
                            elif flag_close == True:
                                self.sleep(1)
                                logger.info("离开派对，请等待...")
                            # elif flag == True or flag_sign == True:
                            elif flag == True  and flag_close == False :
                                logger.info('派对已关闭')
                                break
                        except:
                            logger.info('派对关闭异常')
                        wait_time += 1

    def join_party(self):
        
        pass    