def game():
    import random
    return random.randint(0,100)
def update_score(score, highscore_file="Hi-score.txt"):
    try :
        with open(highscore_file, "r") as file:
          content=file.read()
          if content:
            highscore=int(content)
          else:
            highscore=0
    except FileNotFoundError:
       highscore=0
    if score>highscore:
       print(f"New High Score : {score}")
       with open(highscore_file,"w") as file:
            file.write(str(score))
    else:
       print(f"Current High Score : {highscore}")
def main():
   current_score=game()
   print(f"Current Score : {current_score}")
   update_score(current_score)

if __name__=="__main__":
       main()
              
