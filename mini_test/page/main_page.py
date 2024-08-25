
from airtest.core.api import *
from base.base_airtest import BaseAirtest
from utils.log_util import logger
import re
import math
from utils.config_util import ConfigUtil

class MainPage(BaseAirtest):

    def __init__(self):
        auto_setup(__file__)
        # self.device = connect_device('Android:///')
        self.device = self.set_device()
        # self.device = connect_device("Windows:///?title_re=HiFunClien")
        # self.screen_width = self.device.display_info["height"]
        # self.screen_height = self.device.display_info["width"]
        self.screen_width,self.screen_height = self.get_screen_width()
        super().__init__()




    #等待判定优化打包
    def wait_loading(self, wait_time,*recursive_path):
        wait_time = wait_time
        a = 0
        while a < wait_time:
            try:
                flag = bool(self.exists_recursively_default(*recursive_path))
                logger.info(flag)
                if flag == False :
                    self.sleep(1)
                    logger.info("进行中，请等待...")
                # elif flag == True or flag_sign == True:
                elif flag:
                    logger.info('完成')
                    break
            except:
                logger.info('进行异常')
            a += 1
    #NPC对话点击
    def chat_with_npc(self,*recursive_path):
        self.touch_recursively_default(*recursive_path)
        if not self.exists_recursively_default(*recursive_path):
            print("已进入下一对话")
        else:
            self.touch_recursively_default(*recursive_path)


    #启动游戏打包（已创角）
    def start_test(self):
        self.start_game('com.mico.simsparty.wonderworld')
        if self.exists_recursively_default('main_ui','temp_ui.png'):
            self.touch_recursively_default('main_ui','temp_ui.png')
        self.sleep(5)
        a=0
        while a < 10:
            try:
                # flag = self.exists_recursively_default('main_ui','backpack_icon.png')
                flag = self.exists_recursively_default('main_ui','backpack_text.png')
                flag_sign = self.exists_recursively_default('main_ui','daily_rewards.png')
                logger.info(flag)
                if flag == False and flag_sign == False:
                    self.sleep(1)
                    logger.info("app启动中，请等待...")
                # elif flag == True or flag_sign == True:
                elif flag  or flag_sign :
                    logger.info('启动完成')
                    if flag_sign:
                        self.touch_recursively_default('main_ui','back.png')
                    break
            except:
                logger.info('启动异常')
            a += 1

    #启动游戏打包（未创角）
    def start_test_new(self):
        self.start_game('com.mico.simsparty.wonderworld')
        if self.exists_recursively_default('main_ui','temp_ui.png'):
            self.touch_recursively_default('main_ui','temp_ui.png')
        self.sleep(5)
        a=0
        while a < 10:
            try:
                flag = self.exists_recursively_default('login_ui','all_agree.png')
                logger.info(flag)
                if flag == False :
                    self.sleep(1)
                    logger.info("app启动中，请等待...")
                # elif flag == True or flag_sign == True:
                elif flag :
                    logger.info('启动完成,进入同意协议界面')
                    break
            except:
                logger.info('启动异常')
            a += 1
        if self.exists_recursively_default('login_ui','all_agree.png'):
            self.touch_recursively_default('login_ui','all_agree.png')
            self.wait_loading(20,'login_ui','guide_1.png')
            self.chat_with_npc('login_ui','guide_1.png')
            self.wait_loading(10,'login_ui','guide_2.png')
            self.chat_with_npc('login_ui','guide_2.png')
            self.wait_loading(10,'login_ui','next_step.png')
            self.touch_recursively_default('login_ui','next_step.png')
            self.sleep()
            self.touch_recursively_default('login_ui','submit.png')
            self.sleep()
            self.chat_with_npc('login_ui','guide_finish.png')
            self.sleep(5)
            self.wait_loading(30,'rookie_guide','guide_1.png')

        



    
            
        

    '''以下先将海外版本(简体中文）游戏内的常用按钮等控件元素使用指令打包(验证OK)'''

    #点击虚拟手机
    def wake_phone(self):
        try:
            if self.exists_recursively_default('main_ui','red_phone_icon.png'):
                self.touch_recursively_default('main_ui','red_phone_icon.png')
                #验证是否开启
                if self.exists_recursively_default('main_ui','friend_icon.png'):
                    logger.info('已打开虚拟手机')
                elif self.exists_recursively_default('main_ui','red_phone_icon.png'):
                    self.touch_coordinate(0.96, 0.397) #通过相对坐标点击，建议使用1080*2040分辨率的
                    if self.exists_recursively_default('main_ui','friend_icon.png'):
                        logger.info('已打开虚拟手机')
                    elif self.exists_recursively_default('main_ui','tips.png'):
                        self.error_report()
            elif self.exists_recursively_default('main_ui','phone_icon.png'):
                self.touch_recursively_default('main_ui','phone_icon.png')
                #验证是否开启
                if self.exists_recursively_default('main_ui','friend_icon.png'):
                    logger.info('已打开虚拟手机')
                elif self.exists_recursively_default('main_ui','phone_icon.png'):
                    self.touch_coordinate(0.96, 0.397) #通过相对坐标点击，建议使用1080*2040分辨率的
                    if self.exists_recursively_default('main_ui','friend_icon.png'):
                        logger.info('已打开虚拟手机')
            elif self.exists_recursively_default('main_ui','phone_text.png'):
                self.touch_recursively_default('main_ui','phone_text.png')
                #验证是否开启
                if self.exists_recursively_default('main_ui','friend_icon.png'):
                    logger.info('已打开虚拟手机')
                elif self.exists_recursively_default('main_ui','phone_text.png'):
                    x,y = self.wait_recursively_default('main_ui','phone_text.png')
                    self.touch_coordinate(x,y) #通过相对坐标点击，建议使用1080*2040分辨率的
                    if self.exists_recursively_default('main_ui','friend_icon.png'):
                        logger.info('已打开虚拟手机')                
        except:
            self.error_report()

    def get_erro_text(self):
        erro_file = self.get_snapshot_path("tips_erro.png")        
        self.cut_img(erro_file,612,360,1435,715,"cut_img.png")
        cut_img_path = self.get_snapshot_path("cut_img.png")    
        return cut_img_path
    
    def test_img(self,url):
        erro_file = self.get_erro_text()
        # erro_file = self.get_snapshot_path("tips_erro.png")
        message = self.img_to_string(erro_file)
        print(message)
        # url ="https://open.feishu.cn/open-apis/bot/v2/hook/a4cf4d1a-d6e4-48c8-ba9d-f8eb89e220de"#服务器群的机器人webhook
        self.send_message(url,message)


    def error_report(self):
        if self.exists_recursively_default('main_ui','tips.png'):
            logger.info('服务器报错')
            self.snapshot_img("tips_erro.png")
            erro_file = self.get_snapshot_path("tips_erro.png")
            message = self.img_to_string(erro_file)
            print(message)
            if len(message) > 3:
                config_util = ConfigUtil()
                config = config_util.read_yaml('robot.yaml')
                # 遍历配置文件中的设备信息
                robot_info = config['robot']
                url = robot_info['rul']
                self.test_img(url)
            else:
                print("报错判断失准")


    #传送家园
    def home_tp(self):
        if self.exists_recursively_default('main_ui','home_icon.png'):
            self.touch_recursively_default('main_ui','home_icon.png')
            #验证是否点击传送生效
            try:
                if self.exists_recursively_default('main_ui','home_icon.png'):
                    self.touch_coordinate(0.837, 0.815)#通过相对坐标点击，建议使用1080*2040分辨率的
                    if not self.exists_recursively_default('main_ui','home_icon.png'):
                        logger.info("开始进行传送家园")
                else:
                    logger.info("开始进行传送家园")
            except:
                print("遇到未知错误，待定")                
            finally:
                #判断是否传送完成
                if not self.exists_recursively_default('main_ui','home_details.png'):
                    logger.info("传送家园中")
                    self.sleep(5)
                    wait_time = 0
                    while wait_time < 20:
                        try:
                            flag = bool(self.exists_recursively_default('main_ui','hand_icon.png'))
                            flag_home = bool(self.exists_recursively_default('main_ui','home_details.png'))
                            logger.info(flag)
                            if self.exists_recursively_default('main_ui','tips.png'):
                                self.error_report()
                                break
                            elif flag == False and flag_home == False:
                                self.sleep(1)
                                logger.info("传送中，请等待...")
                            elif flag == True  or flag_home == True :
                                logger.info('已传送家园')
                                break
                        except:
                            logger.info('传送异常')
                        wait_time += 1  


    #传送大世界
    def world_tp(self):
        if self.exists_recursively_default('main_ui','world_icon.png'):
            self.touch_recursively_default('main_ui','world_icon.png')
            #验证是否点击传送生效
            try:
                if self.exists_recursively_default('main_ui','world_icon.png'):
                    self.touch_coordinate(0.837, 0.815)#通过相对坐标点击，建议使用1080*2040分辨率的
                    if not self.exists_recursively_default('main_ui','world_icon.png'):
                        logger.info("开始进行传送大世界")
                else:
                    logger.info("开始进行传送大世界")
            except:
                print("遇到未知错误，待定")                
            finally:
                #判断是否传送完成
                if not self.exists_recursively_default('main_ui','home_details.png'):
                    logger.info("传送大世界中")
                    self.sleep(5)
                    wait_time = 0
                    while wait_time < 20:
                        try:
                            flag = bool(self.exists_recursively_default('main_ui','hand_icon.png'))
                            flag_home = bool(self.exists_recursively_default('main_ui','home_details.png'))
                            logger.info(flag)
                            if self.exists_recursively_default('main_ui','tips.png'):
                                self.error_report()
                                break
                            elif flag == False and flag_home == False:
                                self.sleep(1)
                                logger.info("传送中，请等待...")
                            elif flag == True  and flag_home == False :
                                logger.info('已传送大世界')
                                break
                        except:
                            logger.info('传送异常')
                        wait_time += 1   


    #新手引导处理
    def rookie_guidance(self):
        if self.exists_recursively_default('rookie_guide','guide_1.png'):
            self.swipe((0.6,0.6),(0.7,0.6))#转动视角
            if self.exists_recursively_default('rookie_guide','guide_2.png'):
                """需要固定线路移动到小月旁"""
                self.swipe((0.6,0.6),(0.7,0.6))#移动轮盘
                self.step_move()
                






        pass    

    #打开背包
    def open_backpack(self):
        if self.screen_width == 2400 and self.screen_height ==1080 :
            self.touch_coordinate(0.96, 0.533)
        else:
            if self.exists_recursively_default('main_ui','backpack_icon.png'):
                self.touch_recursively_default('main_ui','backpack_icon.png')
            elif self.exists_recursively_default('main_ui','backpack_text.png'):
                self.touch_recursively_default('main_ui','backpack_text.png')


    #滑动右侧区域查找点击(可用于背包、装扮app等)
    def find_and_touch_element(self,*recursive_path):
        scroll_times = 10
        while scroll_times > 0:
            pos = self.exists_recursively(0.8, *recursive_path)
            if pos:
                touch(pos)
                return
            self.scroll_tab_up()
            scroll_times -= 1
            sleep(2)

    #通过GM控制主角移动
    def move_by_gm(self,poslist):
        if not isinstance(poslist,(list, tuple)):
            poslist = [poslist]
        formatted_poslist = []
        for point in poslist:
            if isinstance(point, (int,float)):
                formatted_pos = f"{point}"
            else:
                formatted_pos = f"{point[0]},{point[1]}"
            formatted_poslist.append(formatted_pos)
        if len(formatted_poslist) == 2:
            if len(formatted_poslist[0].split(',')) == 2:
                poslist_str = '_'.join(formatted_poslist)
            else:
                poslist_str = ','.join(formatted_poslist)
        else:
            poslist_str = '_'.join(formatted_poslist)
        print(poslist_str)
        command = 'walk_by_points %s'%poslist_str
        self.gm_cmd(command)

    
    #轮盘操作主角移动
    def move_around(self,direction='W',duration=0.5):
        if not self.exists_recursively_default('main_ui','tips.png'):
            if self.exists_recursively_default('main_ui','hand_icon.png'):
                self.touch_recursively_default('main_ui','hand_icon.png')
            move_keywords = ["W","A","S","D"]
            vertexs = [(0.13,0.66),(0.07,0.77),(0.13,0.88),(0.19,0.77)]
            swipe_end = vertexs[move_keywords.index(direction)]
            origin = (0.13,0.77)
            platform = self.get_platform()
            if platform == 'Windows':
                self.long_press(direction,duration)
            elif platform == 'Android':
                self.swipe(origin,(swipe_end),duration)
        else:
            self.error_report()

    #获取当前位置坐标
    def get_position(self):
        position_file = self.get_snapshot_path("position.png")  
        self.snapshot_img(position_file)     
        self.cut_img(position_file,1840,998,2272,1062,"position_img.png")
        cut_img_path = self.get_snapshot_path("position_img.png")    
        position = self.img_to_string(cut_img_path)
        position = (self.img_to_string(cut_img_path)).replace("\n","")
        #需要补充坐标为空的情况，需要#初始化获取坐标GM
        if position == '':
            self.gm_cmd('pos')
            position_file = self.get_snapshot_path("position.png")
            self.snapshot_img(position_file)         
            self.cut_img(position_file,1840,998,2272,1062,"position_img.png")
            cut_img_path = self.get_snapshot_path("position_img.png")    
            position = (self.img_to_string(cut_img_path)).replace("\n","")
        return position
    
    #获取当前位置坐标（poco）
    @BaseAirtest.handle_poco_timeout(retries=5, timeout=5)
    def poco_get_position(self):
        if self.poco("root_container").offspring("FUIContainer8106").child("FUIInnerContainer").child("Label").exists():
            position = self.poco("root_container").offspring("FUIContainer8106").child("FUIInnerContainer").child("Label").get_text()
        else:
            self.poco_gm('pos')
            position = self.poco("root_container").offspring("FUIContainer8106").child("FUIInnerContainer").child("Label").get_text()
        return position



    #处理坐标为纯数字
    def clean_coordinate(coordinate_str):
        cleaned_str = re.sub(r'[^\d.-]', '', coordinate_str)
        return cleaned_str

    #移动到指定点
    def step_move(self,end_position):
        start_position = self.get_position().split(",")
        x_start,y_start,z_start = start_position        
        x_end,z_end = end_position
        x_end = float(x_end)
        z_end = float(z_end)
        x_start = float(x_start)
        z_start = float(z_start)
        print(x_start,z_start)
        # 计算两点之间的距离
        distance = math.sqrt((x_end - x_start)**2 + (z_end - z_start)**2)
        # 计算步数
        num_steps = math.ceil(distance / 2)
        intermediate_points = []
        for i in range(num_steps + 1):
            t = i / num_steps
            x = round(x_start + t * (x_end - x_start) ,1)
            z = round(z_start + t * (z_end - z_start) ,1)
            intermediate_points.append((x,z))
        intermediate_points_str = '_'.join(str(p) for p in intermediate_points)
        intermediate_points_str = intermediate_points_str.replace("(","").replace(")","")
        intermediate_points_str= intermediate_points_str.replace(' ','')#去除多余的空格
        print(intermediate_points_str)
        command = 'walk_by_points %s'%intermediate_points_str
        print(command)
        self.gm_cmd(command)
        self.sleep(10)
        return intermediate_points


    def move_step(self,end_position):
        start_position = self.get_position().split(",")
        x_start,y_start,z_start = start_position        
        x_end,z_end = end_position
        x_start = float(x_start)
        z_start = float(z_start)
        intermediate_points = self.step_move(end_position)        
        #移动结果判断
        walk_time = 0
        while walk_time < 10:
            new_pos = self.get_position().split(",")
            new_x = math.floor(float(new_pos[0]))
            new_z = math.floor(float(new_pos[2]))
            if new_x == math.floor(x_end) and new_z == math.floor(z_end):
                print("已到达终点")
                break
            else:
                x_list = []
                z_list = []
                for i in range(3):
                    new_pos = self.get_position().split(",")
                    new_x = math.floor(float(new_pos[0]))
                    new_z = math.floor(float(new_pos[2]))
                    x_list.append(new_x)
                    z_list.append(new_z)
                if x_list.count(x_list[0]) == 3 and z_list.count(z_list[0]) == 3 :
                    if x_start < x_end and z_start < z_end:
                        for i,pos in intermediate_points:
                            if pos[0] >= x_list[0] and pos[1] >= z_list[0]:
                                back_pos = intermediate_points[i-1]
                                next_pos = (back_pos[0]+2,back_pos[1])
                                return back_pos,new_pos
                    elif x_start > x_end and z_start > z_end:
                        for i,pos in intermediate_points:
                            if pos[0] <= x_list[0] and pos[1] <= z_list[0]:
                                back_pos = intermediate_points[i-1]
                                next_pos = (back_pos[0]-2,back_pos[1])
                                return back_pos,new_pos
                    elif x_start < x_end and z_start > z_end:
                        for i,pos in intermediate_points:
                            if pos[0] >= x_list[0] and pos[1] <= z_list[0]:
                                back_pos = intermediate_points[i-1]
                                next_pos = (back_pos[0]+2,back_pos[1])
                                return back_pos,next_pos
                    elif x_start > x_end and z_start < z_end:
                        for i,pos in intermediate_points:
                            if pos[0] <= x_list[0] and pos[1] >= z_list[0]:
                                back_pos = intermediate_points[i-1]
                                next_pos = (back_pos[0]-2,back_pos[1])
                                return back_pos,next_pos
                    self.move_by_gm(back_pos)
                    self.sleep(2)
                    self.move_by_gm(next_pos)
                    self.sleep(1)
                    self.move_by_gm(end_position)


        
        
        

    #使用gm执行命令窗口
    def gm_cmd(self,command):
        if self.exists_recursively_default('main_ui','gm.png'):
            self.touch_recursively_default('main_ui','gm.png')
            #判断是否开启GM面板
            if self.exists_recursively_default('main_ui','gm_execute.png'):
                self.touch_recursively_default('main_ui','clean_input.png')
                x,y= self.wait_recursively_default('main_ui','gm_execute.png')
                self.touch_coord(x-200, y)#通过坐标点击
                self.sleep(1.0)
                # self.delete_text(30)
                self.input_text(command)
                self.touch_coord(x-200, y+200)
                self.touch_recursively_default('main_ui','gm_execute.png')
                self.sleep(1.0)
                self.touch_recursively_default('main_ui','gm_close.png')
                self.sleep(1.0)
                if self.exists_recursively_default('main_ui','gm_close.png'):
                    self.touch_coordinate(0.698, 0.825)
        else:
            raise Exception('GM not initialized')

    
    #GM进场景
    def enter_by_gm(self,command):
        self.gm_cmd(command)
        #判断是否传送完成
        if not self.exists_recursively_default('main_ui','hand_icon.png'):
            logger.info("传送中")
            self.sleep(5)
            wait_time = 0
            while wait_time < 20:
                try:
                    flag = bool(self.exists_recursively_default('main_ui','hand_icon.png'))
                    logger.info(flag)
                    if self.exists_recursively_default('main_ui','tips.png'):
                        self.error_report()
                        break
                    elif flag == False:
                        self.sleep(1)
                        logger.info("传送中，请等待...")
                    elif flag == True:
                        logger.info('已传送完成')
                        break
                except:
                    logger.info('传送异常')
                wait_time += 1    


    #GM进场景-房屋
    def inroom(self):
        self.enter_by_gm('inroom')
    
    #GM进场景-理发店
    def goto_hair_salon(self):
        self.enter_by_gm('goto_hair_salon')

    #GM进场景-大型商城
    def goto_shop(self):
        self.enter_by_gm('goto_shop')

    #GM进场景-露营地
    def goto_camp(self):
        self.enter_by_gm('goto_camp')

    #GM进场景-服装店
    def goto_cloth(self):
        self.enter_by_gm('goto_cloth')
        

    def stop_game_now(self):
        self.stop_game('com.mico.simsparty.wonderworld')
        
    #点击返回按钮（通用）
    def touch_back(self):
        if self.exists_recursively_default('main_ui','back.png'):
            self.touch_recursively_default('main_ui','back.png')
            self.sleep()
        
    #判断程序是否崩溃
    def is_crash(self,pagename='com.mico.simsparty.wonderworld'):
        try:
            pid =  self.adb_shell('pidof %s'%pagename)
        except:
            print("App is not running")
            return True
        print(f"App is running with pid: {pid}")
        return False
    

    #关闭&开启交互方向&距离判断
    def operate_reinforce(self,on_off=True):
        if on_off:
            self.gm_cmd('operate_reinforce')
        else:
            self.gm_cmd('close_operate_reinforce')







#
# MainPage().start_test()
# MainPage().wake_phone()
