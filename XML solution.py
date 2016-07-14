from xml.etree import ElementTree
import re

class Edit_XML_file():
    def __init__(self, path):
        with open(path, 'rt') as f:
            self.tree = ElementTree.parse(f)   
                        
    def read_xml(self, in_path):
        '''''读取并解析XML文件
            in_path: xml路径
            return: ElementTree'''
        self.tree.parse(in_path)
            
    def write_xml(self,out_path):
        '''''将xml文件写出
            tree:xml树
            out_path: 写出路径'''
        self.tree.write(out_path, encoding="utf-8" , xml_declaration=True)
            
    def find_the_node(self, path):
        '''''查找某个路径匹配的第一个节点
            tree: xml树
            path: 节点路径'''
        return self.tree.find(path)
        
    def find_all_the_node(self, path):
        '''''查考某个路径匹配的所有节点
            tree: xml树
            path: 节点路径'''
        return self.tree.findall(path) #this is a list value
        
    def read_the_node(self, nodelist):
        '''''读取某个节点的文本属性
            nodelist:节点名称'''
        return nodelist.text
        
    def change_node_text(self, nodelist, text):
        '''''更改节点的文本
            nodelist: 节点
            text:文本内容'''
        nodelist.text = text
        
    #def create_node(self, tag, property_map, content):
        '''''新造一个节点
            tag:节点标签
            property_map:属性及属性值map
            content:节点闭合标签里的文本内容
            return 新节点'''
        #element = Element(tag, property_map)
        #element.text = content
        #return element
        
    # def add_child_node(self, nodelist, element):
    #     '''''给一个节点添加子节点
    #         nodelist: 节点列表
    #         element: 子节点'''
    #     for node in nodelist:
    #         node.append(element)
        
#路径设定
xml_file_path = 'C:/Users/Bob.Yao/Python/mc.xml'

#创建一个对象
control_xml = Edit_XML_file(xml_file_path)

#找到节点
# account_node = control_xml.find_the_node("./account/text")
# pwd_node = control_xml.find_the_node("./pwd/text")
# Tag_Number_tag35 = control_xml.find_the_node("./TagNumber/tag35")

#找到根节点
root_node = control_xml.find_the_node(".")
#print (root_node)

#找到节点组
node_temp = []

upstream_msg = control_xml.find_all_the_node("./upmsg") #得到所有上游message的树结构



for upstream_msg_list in upstream_msg: #遍历所有upstream里面的每一个节点列表
    upstream_msg_value = control_xml.read_the_node(upstream_msg_list)
    node_temp.append(upstream_msg_value) #上游message信息 都存到了数组里面
    #print (upstream_msg_value)

#print (node_temp)

#def addPara_to_dic(theIndex, Para, Val):
    #theIndex.setdefault(Para, []).append(Val)

dict_temp = {}
dict_output = []


def create_node(tag, property_map, content):
    '''''新造一个节点
        tag:节点标签
        property_map:属性及属性值map
        content:节点闭合标签里的文本内容
        return 新节点'''
    element = Element(tag, property_map)
    element.text = content
    return element 
    
def add_child_node(nodelist, element):
    '''''给一个节点添加子节点
        nodelist: 节点列表
        element: 子节点'''
    #for node in nodelist:
    nodelist.append(element)

#定义一个函数传入一个节点组（上游节点组的具体值信息）

for node_temp_value in node_temp:
    #print (node_temp_value) #找到上游的message信息
    list_temp = re.findall("(?<=\^)[^\^]*(?=\^)", node_temp_value)
    #str_t='text'
    #print (list_temp) #在每一段upstream message里面取出所有满足正则表达式的值
    for str_tag in list_temp:
        #print (str_tag) #把满足正则表达式tag number = tag value的每一个值 按等号“=”左右两边拆分
        strPara = str_tag.split('=')[0]
        strVal = str_tag.split('=')[1]
        #print (strPara)
        #print (strVal)
        dict_temp[strPara] = strVal
        
    strPara ='text'
    strVal = node_temp_value
    dict_temp[strPara] = strVal
    #拆分后再存到一个临时的词典dict_temp里面
    #print (dict_temp)
    dict_output.append(dict_temp) #把每个词典存到一个临时的序列里面，一个词典代表一行上游的message
#print (dict_output)

new_node_list_temp = [] #建立一个临时的新节点序列
new_node_list = []

for dict_out_item in dict_output: #取出每一个词典的值 - 分别代表一行上游的message （按照词典的格式）
    #print (dict_out_item)  # this is a dictionary
    for dict_out_item_eachvalue in dict_out_item.items():
        tag_number_ID = dict_out_item_eachvalue[0]
        #print (dict_out_item_eachvalue[0])
        tag_number_value = dict_out_item_eachvalue[1]
        #print (dict_out_item_eachvalue[1])
        #取出词典里面的每一对hash值 每一个生成一个新的节点 
        
        new_node = create_node("tag number", {"ID":tag_number_ID} ,tag_number_value)
        #print (new_node.get("ID"))
        new_node_list_temp.append(new_node)
    #print (new_node_list_temp)
    new_node_list.append(new_node_list_temp)
#print (new_node_list) #打印出最后生成的新节点组

#增加一个新节点
    #A.新建节点  
a = create_node("upstream_message_tag_info", {"test1":"15","test2":"20"}, "this is the first content")

#print (a)
    #B.插入到根节点之下  
add_child_node(root_node, a)  

#找到upstream 新增的节点
upstream_message_tag_info_node = control_xml.find_the_node("./upstream_message_tag_info")
#print (upstream_message_tag_info_node)

for new_node_list_item in new_node_list:
    #print (new_node_list_item)
    for each_node in new_node_list_item:
        #print ("\n###########################\n")
        print (each_node.get("ID"))
        #print (each_node)
        add_child_node(upstream_message_tag_info_node, each_node)
        #print ("\n###########end################\n")

#print (create_node("tag number", {"ID":"15"} ,"HK"))

#删除节点
#for upstream_msg_list in upstream_msg:
    #root_node.remove(upstream_msg_list)

#读取节点文本
# username_box_value = 0
# password_box_value = 0
# username_box_value = control_xml.read_the_node(account_node)
# password_box_value = control_xml.read_the_node(pwd_node)
#Tag_Number_tag35_value = control_xml.read_the_node(Tag_Number_tag35)


#更改节点文本
#control_xml.change_node_text(account_node, "yaobob")
#control_xml.change_node_text(pwd_node, "CHROME@201609")


#增加子节点


#将xml文件写出
#control_xml.write_xml(xml_file_path)
