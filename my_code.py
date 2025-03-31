import pytest

def fix_phone_num(phone_num_to_fix):
  # given "5125558823". Split the parts, then recombine and return
  # if (len(phone_num_to_fix) != 10):
  #   raise ValueError("Can only format numbers that are exactly 10 digits long")
  
  # if not phone_num_to_fix.isdigit():
  #   raise ValueError("All values must be digits")
  
  num = ""
  digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  for val in phone_num_to_fix:
    if val in digits:
      print(val)
      num = num + val
  
  area_code = num[0:3] # 512 (first three digits)
  three_part = num[3:6] # 555 (next three digits)
  four_part = num[len(num) -4 :len(num)] # # 8823 (last four digits)
  print(f"code: {area_code}")
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_fix_phone_num2():
  assert fix_phone_num("555-442-98761") == "(555) 442 8761"
  assert fix_phone_num("(321) 654 3333") == "(321) 654 3333"

def test_fixe_phone_num3():
  with pytest.raises(ValueError):
    fix_phone_num("51")

def test_fixe_phone_num4():
  with pytest.raises(ValueError):
    fix_phone_num("555-442-9876")