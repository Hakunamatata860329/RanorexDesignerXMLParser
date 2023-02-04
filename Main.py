from xml.etree.cElementTree import ElementTree, Element
import xml.etree.ElementTree as ET
import csv
import pandas as pd
import re

tree = ET.parse('DIADesigner_New_Test.rxtst')
DesignerTestSuite = tree.getroot()

modifynode = "TestHaveOneCondition"
runTestContainer = "OR"
runDeviceMatch = "IsEqual"

def insertLeftValue():
    leftValue = ET.Element("datavaluesource")
    leftValue.set("bindingtype", "DataConnector")
    leftValue.set("dataname", "Path1")
    leftValue.set("id", "25732418-477c-4426-8f73-723965fb45d3") 

def insertRightValue():
    rightValue = ET.Element("simplevaluesource")
    rightValue.set("value", "AS300")

for testSuitedoc in DesignerTestSuite:
   for flatlistofchildren in testSuitedoc.iter("flatlistofchildren"):
        for smartfoldernode in flatlistofchildren.iter("smartfoldernode"):
            # print(smartfoldernode.attrib["name"], smartfoldernode.iter("conditiongroup"))
            if  smartfoldernode.attrib["name"] == modifynode:
                # print(smartfoldernode.attrib["name"], smartfoldernode.attrib)
                for conditiongroup in smartfoldernode.iter("conditiongroup"):
                    conditiongroup.set("comparison", runTestContainer)
                    conditiongroup.set("enabled", "True")
                    conditiongroup.remove(conditiongroup.find("condition"))
                    conditiongroup.insert(0, ET.Element('condition'))
                    for condition in conditiongroup.iter("condition"):
                        condition.set("comparison", runDeviceMatch)
                        condition.insert(0, ET.Element("leftValue"))
                        for leftValueContent in condition.iter("leftValue"):
                            leftValueContent.insert(0, insertLeftValue())
                        condition.insert(1, ET.Element("rightValue"))
                        for leftValueContent in condition.iter("rightValue"):
                            leftValueContent.insert(0, insertRightValue())
tree.write("Test.xml")