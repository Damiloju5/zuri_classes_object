class Student:
   
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        

    def change_name(self, name):
        if(name != self.name):
           self.name = name
           print(self.name)
        else:
          print("same name")
       
    def change_age(self, age):
        if(age != self.age):
          self.age = int(age)
          print(self.age)
        else:
          print("same age")
       
    def add_track(self, track):
        if(track in self.tracks):
          print("track exists")
        else:
          self.tracks.append(track)
          print(self.tracks)
    def get_score(self):
        print(self.score)
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob.change_name("Bob")
Bob.change_age(26)
Bob.add_track("FE")
Bob.get_score()
print("......................")
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()