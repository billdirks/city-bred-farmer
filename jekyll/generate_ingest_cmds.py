# Path to files
path = "../../RawDocx/20250201/"

# To get filenames run this in directory with files
#  % for x in *; do echo \    "$x\"\,; done | xargs -0
files = [
    "CBF #100, Feb. 9, 1948.docx",
    "CBF #101_ Feb. 16, 1948.docx",
    "CBF #102_ Feb. 23, 1948.docx",
    "CBF #103_ March 1, 1948.docx",
    "CBF #104_ March 8, 1948.docx",
    "CBF #105_ March 15, 1948.docx",
    "CBF #106_ March 22, 1948.docx",
    "CBF #107_ March 29, 1948.docx",
    "CBF #108_ April 5, 1948.docx",
    "CBF #109_ April 12, 1948.docx",
    "CBF #110_ April 19, 1948.docx",
    "CBF #111_ April 26, 1948.docx",
    "CBF #112_ May 3, 1948.docx",
    "CBF #113_ May 10, 1948.docx",
    "CBF #114_ May 11, 1948.docx",
    "CBF #115_ May 12, 1948.docx",
    "CBF #119_ May 18, 1948.docx",
    "CBF #120_ May 19, 1948.docx",
    "CBF #121_ May 20, 1948.docx",
    "CBF #123_ May 24, 1948.docx",
    "CBF #124_ May 25, 1948.docx",
    "CBF #125_ May 26, 1948.docx",
    "CBF #126_ May 27, 1948.docx",
    "CBF #127_ May 28, 1948.docx",
    "CBF #128_ May 31, 1948.docx",
    "CBF #53; May 5, 1947.docx",
    "CBF #54_ May 12, 1947.docx",
    "CBF #55_ May 19, 1947.docx",
    "CBF #56_ May 26, 1947.docx",
    "CBF #57_ June 2, 1947.docx",
    "CBF #58_ June 9, 1947.docx",
    "CBF #59_ June 16, 1947.docx",
    "CBF #60_ June 23, 1947.docx",
    "CBF #61_ June 30, 1947.docx",
    "CBF #62_ July 7, 1947.docx",
    "CBF #63_ July 14, 1947.docx",
    "CBF #64_ July 21, 1947.docx",
    "CBF #65_ July 28, 1947.docx",
    "CBF #66_ Aug. 4, 1947.docx",
    "CBF #67_ Aug. 11, 1947.docx",
    "CBF #68_ Aug. 18, 1947.docx",
    "CBF #69_ Aug. 25, 1947.docx",
    "CBF #70_ Sept. 1, 1947.docx",
    "CBF #71_ Sept. 3, 1947.docx",
    "CBF #72_ Sept. 5, 1947.docx",
    "CBF #73_ Sept. 7, 1947.docx",
    "CBF #75_ Sept. 8, 1947.docx",
    "CBF #76_ Sept. 15, 1947.docx",
    "CBF #77_ Sept. 17, 1947.docx",
    "CBF #78_ Sept. 22, 1947.docx",
    "CBF #79_ Sept. 29, 1947.docx",
    "CBF #80_ Oct. 6, 1947.docx",
    "CBF #81_ Oct. 13, 1947.docx",
    "CBF #82_ Oct. 20, 1947.docx",
    "CBF #83_ Oct. 27, 1947.docx",
    "CBF #84_ Nov. 3, 1947.docx",
    "CBF #85_ Nov. 6, 1947.docx",
    "CBF #86_ Nov. 7, 1947.docx",
    "CBF #87_ Nov. 10, 1947.docx",
    "CBF #88_ Nov. 17, 1947.docx",
    "CBF #89_ Nov. 24, 1947.docx",
    "CBF #90_ Dec. 1, 1947.docx",
    "CBF #91_ Dec. 8, 1947.docx",
    "CBF #92_ Dec. 15, 1947.docx",
    "CBF #93_ Dec. 22, 1947.docx",
    "CBF #94_ Dec. 29, 1947.docx",
    "CBF #95_ Jan. 5, 1948.docx",
    "CBF #96_ Jan. 12, 1948.docx",
    "CBF #97_ Jan. 19, 1948.docx",
    "CBF #98_ Jan. 26, 1948.docx",
    "CBF #99_ Feb. 2, 1948.docx",
    "CBF 116_ May 13, 1948.docx",
    "CBF 117_ May14, 1948.docx",
    "CBF 118_ May 17, 1948.docx",
    "CBF @122_ May 21, 1948.docx",
]

def to_month(filename: str) -> str:
    fn = filename.casefold()
    if "jan" in fn:
        return "01"
    elif "feb" in fn:
        return "02"
    elif "mar" in fn:
        return "03"
    elif "apr" in fn:
        return "04"
    elif "may" in fn:
        return "05"
    elif "jun" in fn:
        return "06"
    elif "jul" in fn:
        return "07"
    elif "aug" in fn:
        return "08"
    elif "sep" in fn:
        return "09"
    elif "oct" in fn:
        return "10"
    elif "nov" in fn:
        return "11"
    elif "dec" in fn:
        return "12"
    raise Exception("no month found")

def parse_date(filename: str) -> tuple[str, str, str]:
    year = filename[-9:-5]
    day = filename[-13:-11]
    day = day if day[0] != " " else f"0{day[1]}"
    month = to_month(filename)
    return (year, str(month), day)

if __name__ == '__main__':
    for f in sorted(files, key=parse_date):
        year, month, day = parse_date(f)
        print(f'python3 ./ingest_docx.py --date {year}{month}{day} --docx "{path}{f}"')
