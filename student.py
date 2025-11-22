import sys

if len(sys.argv) == 3:
    script_name=sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("user provided input values:")
else:
  script_name = sys.argv[0] 
  name = "somu"
  rollno = "bca307"
  print("no input given -using default values")

print("script name :", script_name)
print("student name :", name)
print("roll number :", rollno)
