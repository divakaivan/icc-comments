# Copyright (c) 2018 The Python Packaging Authority
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def generate_comment(text, type_of=None):
    """
    Generate big hash-tag statements. Very good for eye-catching success/warning/fail messages.
    Or just to generate a BIG has-tag comment to easily distinguish code in thousands lines of code.

    Args:
        text: str: String of the text you want to get generated.
        type_of: str: Color of the the printed statement. Default is None, which is the default print color of your IDE.

    Returns:
        Hash-tag created text.
    """
    char_dict = {
        "a": """
#####
#   #
#####
#   #
#   #
              """,
        "b": """
#### 
##  #
#### 
##  #
#### 
              """,
        "c": """
 ####
##   
##   
##   
 ####
              """,
        "d": """
#### 
##  #
##  #
##  #
#### 
              """,
        "e": """
#####
##   
#### 
##   
#####
              """,
        "f": """
#####
##   
#### 
##   
##   
              """,
        "g": """
 ####
#    
#### 
#   #
 ### 
              """,
        "h": """
##  ##
##  ##
######
##  ##
##  ##
              """,
        "i": """
#####
  #  
  #  
  #  
#####
              """,
        "j": """
#####
  #  
  #  
  #  
##   
              """,
        "k": """
##  #
## # 
##   
## # 
##  #
              """,
        "l": """
##   
##   
##   
##   
#####
              """,
        "m": """
#   #
## ##
# # #
#   #
#   #
              """,
        "n": """
#   #
##  #
# # #
#  ##
#   #
              """,
        "o": """
 ### 
#   #
#   #
#   #
 ### 
              """,
        "p": """
#####
##  #
#####
##   
##   
              """,
        "q": """
 ### 
#   #
#   #
#  ##
 ####
              """,
        "r": """
#####
##  #
#####
## # 
##  #
              """,
        "s": """
 ### 
#    
 ### 
    #
 ### 
              """,
        "t": """
#####
  #  
  #  
  #  
  #  
              """,
        "u": """
## ##
## ##
## ##
## ##
 ### 
              """,
        "v": """
## ##
## ##
## ##
## ##
 ### 
              """,
        "w": """
##         ##
##   ###   ##
##  ## ##  ##
##  ## ##  ##
 ####   #### 
              """,
        "x": """
# # 
# # 
 #  
# # 
# # 
              """,
        "y": """
#   #
 # # 
  #  
  #  
  #  
              """,
        "z": """
#####
   # 
  #  
 #   
#####
              """,
        " ": """
  
  
  
  
  
        """,
        "0" : """
 ### 
#   #
#   #
#   #
 ### 
              """,
        "1" : """
  ## 
 ### 
# ## 
  ## 
  ## 
              """,
        "2" : """
 ### 
#   #
   # 
  #  
#####
              """,
        "3" : """
 ### 
    #
  ## 
    #
 ### 
              """,
        "4" : """
  ## 
 # # 
#####
   # 
   # 
              """,
        "5" : """
#####
#    
#### 
    #
 ### 
              """,
        "6" : """
#####
#    
#####
#   #
#####
              """,
        "7" : """
#####
   # 
  #  
 #   
#    
              """,
        "8" : """
 ### 
#   #
 ### 
#   #
 ### 
              """,
        "9" : """
 ### 
#   #
 ####
    #
 ### 
              """
    }
    text_letters = [char_dict[i.lower()].splitlines() for i in text]
    color_dict = {
        "warn" : "\033[93m",
        "success" : "\033[0;32m",
        "fail" : "\033[1;31m",
        None: ""
    }
    for lines in zip(*text_letters):
        print(f'{color_dict[type_of]}{"  ".join(x for x in lines)}{color_dict[type_of]}')


generate_comment("abcdefghijklmnopqrstuvwxyz 0123456789")

