import csv 

# csv 파일로 뽑아내는 함수
def save_to_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])

  for job in jobs:
    writer.writerow(list(job.values()))
  return 