from page.main_page import MainPage
from utils.log_util import logger
from airtest.core.api import *
from airtest.aircv import *
from utils.config_util import ConfigUtil




class HomePage(MainPage):

    #钓鱼
    def fishing(self):
        while True:
            if self.exists_recursively_default('main_ui','fishing.png'):
                for i in range(20):
                    self.touch_coordinate(0.89,0.77)
                    self.sleep(0.1)
                    print('溜鱼')
            if self.exists_recursively_default('main_ui','accept.png'):
                self.touch_recursively_default('main_ui','accept.png')
                print('钓鱼成功')
                self.sleep(2)
                break
            if self.exists_recursively_default('main_ui','x.png'):
                self.touch_coordinate(0.89,0.77)
                self.sleep(5)
                    

    #摇树
    def shaking_tree(self):
        if self.exists_recursively_default('interaction','Main_icon_shake.png'):
            self.touch_recursively_default('interaction','Main_icon_shake.png')


    #砍树
    def cut_down_tree(self):
        if self.exists_recursively_default('interaction','Main_icon_cutdown.png'):
            self.touch_recursively_default('interaction','Main_icon_cutdown.png')

    #挖矿
    def mining(self):
        if self.exists_recursively_default('interaction','Main_icon_mining.png'):
            self.touch_recursively_default('interaction','Main_icon_mining.png')

    #拾取
    def pickup(self):
        if self.exists_recursively_default('interaction','Main_icon_pick.png'):
            self.touch_recursively_default('interaction','Main_icon_pick.png')

    #NPC对话
    def chat_with_npc(self):
        if self.exists_recursively_default('interaction','task_icon_11.png'):
            self.touch_recursively_default('interaction','task_icon_11.png')
            self.sleep(1.0)


    #与指定NPC对话
    def chat_appoint_npc(self,npc_name):
        self.config = ConfigUtil()
        npc_position = self.config.get_yaml_value('npc.yaml','npc',npc_name)
        if npc_position != None:
            npc_position = npc_position.split(",")
            self.step_move(npc_position)
            self.chat_with_npc()    
        else:
            raise Exception('The NPC does not exist')   
            

    #岛屿扩建
    def expand_island(self):
        self.chat_appoint_npc('Nicks')
        if self.exists_recursively_default():
            self.touch_recursively_default()
            self.wait_recursively_default()
            self.touch_recursively_default()

    

