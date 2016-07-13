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
        
    def add_child_node(self, nodelist, element):
        '''''给一个节点添加子节点
            nodelist: 节点列表
            element: 子节点'''
        for node in nodelist:
            node.append(element)
        
#路径设定
xml_file_path = 'C:/Users/Bob.Yao/Python/mc.xml'

#创建一个对象
control_xml = Edit_XML_file(xml_file_path)

#找到节点
# account_node = control_xml.find_the_node("./account/text")
# pwd_node = control_xml.find_the_node("./pwd/text")
# Tag_Number_tag35 = control_xml.find_the_node("./TagNumber/tag35")

#找到节点组
node_temp = []

upstream_msg = control_xml.find_all_the_node("./upmsg")
for upstream_msg_list in upstream_msg:
    upstream_msg_value = control_xml.read_the_node(upstream_msg_list)
    node_temp.append(upstream_msg_value)
    #print (upstream_msg_value)

#print (node_temp)

#def addPara_to_dic(theIndex, Para, Val):
    #theIndex.setdefault(Para, []).append(Val)

dict_temp = {}
dict_output = []

for node_temp_value in node_temp:
    #print (node_temp_value)
    list_temp = re.findall("(?<=\^)[^\^]*(?=\^)", node_temp_value)
    #print (list_temp)
    for str_tag in list_temp:
        #print (str_tag)
        strPara = str_tag.split('=')[0]
        strVal = str_tag.split('=')[1]
        #print (strPara)
        #print (strVal)
        dict_temp[strPara] = strVal
    #print (dict_temp)
    dict_output.append(dict_temp)
#print (dict_output)

for dict_out_item in dict_output:
    #print (dict_out_item)  # this is a dictionary
        for dict_out_item_eachvalue in dict_out_item.items():
            #print (dict_out_item_eachvalue[0])
            print (dict_out_item_eachvalue[1])
            #new_node = control_xml.create_node(dict_out_item_eachvalue[0])
        
def create_node(tag, property_map, content):
    '''''新造一个节点
        tag:节点标签
        property_map:属性及属性值map
        content:节点闭合标签里的文本内容
        return 新节点'''
    element = Element(tag, property_map)
    element.text = content
    return element 
           
create_node("100", {"value":"15"} ,"HK")


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
