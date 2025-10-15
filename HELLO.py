from cobol_variable import *
import importlib, inspect, os, sys
# PROGRAM-ID: HELLO
class HELLOClass:
    def __init__(self):
        self.is_batch = True
        self.call_result = None
        self.terminate = False
        self.paragraph_list = []
        self.last_fallthrough_paragraph = 0
        self.debug_line = '0'
        self.error_triggered = False
        self.calling_module = None
        self.HELLOMemory = EMPTY_STRING
        self.EIBMemory = EMPTY_STRING
        self.SPECIALREGISTERSMemory = EMPTY_STRING
        self.variables_list = []
        self._INTERNALVars = []
        self.variables_list.append(self._INTERNALVars)
        self._INTERNALVars = Add_Variable('', self._INTERNALVars, 'MODULE-NAME', 0, 'X', 'MODULE-NAME', '', 0, 0, '', '01')[0]
        self._INTERNALVars[0].value = 'HELLO'
        self._INTERNALVars[0].address_module = AddressModule(self, 0)
        self._INTERNALVars = Add_Variable('', self._INTERNALVars, 'CALLING-MODULE-NAME', 0, 'X', 'CALLING-MODULE-NAME', '', 0, 0, '', '01')[0]
        self._INTERNALVars = Add_Variable(self.SPECIALREGISTERSMemory, self._INTERNALVars, 'SORT-RETURN', 4, '9', 'SORT-RETURN', '', 0, 0, '', '01')[0]
        self._INTERNALVars = Add_Variable(self.SPECIALREGISTERSMemory, self._INTERNALVars, 'RETURN-CODE', 4, '9', 'RETURN-CODE', '', 0, 0, '', '01')[0]
        result = Allocate_Memory(self._INTERNALVars,self.SPECIALREGISTERSMemory)
        self._INTERNALVars = result[0]
        self.SPECIALREGISTERSMemory = result[1]
        self.SPECIALREGISTERSMemory = Set_Variable(self.SPECIALREGISTERSMemory,self.variables_list,'SORT-RETURN', 0,'SORT-RETURN')[1]
        self.SPECIALREGISTERSMemory = Set_Variable(self.SPECIALREGISTERSMemory,self.variables_list,'RETURN-CODE', 0,'RETURN-CODE')[1]
        self.error_func = None
        self.calling_module = None
        self.job_name = EMPTY_STRING
        self.job_step = EMPTY_STRING
        self.dd_name_list = []
        self._DataDivisionVars = []
        self.variables_list.append(self._DataDivisionVars)
        self.EIBList = []
        self.variables_list.append(self.EIBList)
        self._FILE_CONTROLVars = []
        initialize()
        self.initialize2()
# DATA DIVISION
# WORKING-STORAGE SECTION.
        self._DataDivisionVars = Add_Variable(self.HELLOMemory,self._DataDivisionVars,'USER-NAME', 20, 'A','USER-NAME','',0,0,'','01','',False,'')[0]
        result = Allocate_Memory(self._DataDivisionVars,self.HELLOMemory)
        self._DataDivisionVars = result[0]
        self.HELLOMemory = result[1]
# EIB Fields
# PROCEDURE DIVISION
    def main(self,caller,*therest):
        try:
            self.EIBMemory=Retrieve_EIB_Area(self._INTERNALVars[0].value)
            self.calling_module = caller
            self._INTERNALVars[1].value = '&&*'
            self._INTERNALVars[1].address_module = AddressModule(caller, 0)
            self.debug_line = '7'
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'"ENTER','"ENTER',False,False)
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'YOUR','YOUR',False,False)
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'NAME:','NAME:',False,False)
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'"','"',False,False)
            self.debug_line = '8'
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'','literal',True,True)
            self.HELLOMemory = Set_Variable(self.HELLOMemory,self.variables_list,'USER-NAME','__ACCEPT ','USER-NAME')[1]
            self.debug_line = '9'
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'"HELLO,','"HELLO,',False,False)
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'"','"',False,False)
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'USER-NAME','USER-NAME',False,False)
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'"!"','"!"',False,False)
            self.debug_line = '10'
            Display_Variable(self.calling_module, self.HELLOMemory,self.variables_list,'','literal',True,True)
            #inform calling module that termination has happened
            self.calling_module.terminate_on_callback()
            return []
        except Exception as e:
            self._error_handler(e)

    def initialize2(self):
        self.is_batch = True
        return

    def default_fallthrough(self):
        if len(self.paragraph_list) > self.last_fallthrough_paragraph:
            exec('self.' + self.paragraph_list[self.last_fallthrough_paragraph] + '(True)')
        return

    def fallthrough(self, name):
        if self.error_triggered:
            return
        count = 0
        for pl in self.paragraph_list:
            if pl == name and count + 1 < len(self.paragraph_list):
                self.last_fallthrough_paragraph = count + 1
                # jump to the next paragraph
                exec('self.' + self.paragraph_list[count + 1] + '(True)')
                break
            count = count + 1
        return

    def retrieve_pointer(self, name):
        return Get_Variable_Value(self.HELLOMemory,self.variables_list,name, name)

    def set_value(self, name, value):
        self.HELLOMemory = Set_Variable(self.HELLOMemory,self.variables_list,name, value, name)[1]
        return

    def get_value(self, name):
        return Get_Variable_Value(self.HELLOMemory, self.variables_list, name, name)

    def print_out(self, val, end_l):
        print(val, end=end_l)
        return

    def receive_control(self):
        pass

    def get_return_code(self):
        return Get_Variable_Value(self.SPECIALREGISTERSMemory,self.variables_list,"RETURN-CODE", "RETURN-CODE")

    def terminate_on_callback(self):
        self.terminate = True
        return

    def get_dd_value(self, value: str):
        result = 'UNKNOWN'
        for dd in self.dd_name_list:
            if len(dd) > 1:
                if dd[0].strip() == value.strip():
                    result = dd[1].strip()
                    break
        return result

    def process_key(self, keycode: int):
        return CheckAttentionKey(keycode)

    def _error_handler(self, e):
        self.error_triggered = True
        if self.error_func != None:
            self.error_func()
        else:
            self.SPECIALREGISTERSMemory = Set_Variable(self.SPECIALREGISTERSMemory,self.variables_list,'RETURN-CODE', 12,'RETURN-CODE')[1]
            print('')
            print('error encountered:')
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print('COBOL Source File:      ./cobol_tests/COBALTEST.cbl')
            print('COBOL File Line Number: ' + self.debug_line)
        return

if __name__ == '__main__':
    main_obj = HELLOClass()
    main_obj.main(main_obj)
    Cleanup()

