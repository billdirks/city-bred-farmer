# Path to files
path = "../../RawDocx/20250312/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #206_ Sept. 15, 1948.docx",
    "CBF #207_ Sept. 16, 1948.docx",
    "CBF #208_ Sept. 17, 1948.docx",
    "CBF #209_ Sept. 18, 1948.docx",
    "CBF #210_ Sept. 19, 1948.docx",
    "CBF #211_ Sept. 20, 1948.docx",
    "CBF #212_ Sept. 21, 1948.docx",
    "CBF #213_ Sept. 22, 1948.docx",
    "CBF #214_ Sept. 23, 1948.docx",
    "CBF #215_ Sept. 24, 1948.docx",
    "CBF #216_ Sept. 25, 1948.docx",
    "CBF #217_ Sept. 26, 1948.docx",
    "CBF #218_ Sept. 27, 1948.docx",
    "CBF #219_ Sept. 28, 1948.docx",
    "CBF #220_ Sept. 29, 1948.docx",
    "CBF #221_ Sept. 30, 1948.docx",
    "CBF #222_ Oct. 1, 1948.docx",
    "CBF #223_ Oct. 4, 1948.docx",
    "CBF #224_ Oct. 5, 1948.docx",
    "CBF #225_ Oct. 6, 1948.docx",
    "CBF #226_ Oct. 7, 1948.docx",
    "CBF #227_ Oct. 8, 1948.docx",
    "CBF #228_ Oct. 11, 1948.docx",
    "CBF #229_ Oct. 12, 1948.docx",
    "CBF #230_ Oct. 13, 1948.docx",
    "CBF #231_ Oct. 14, 1948.docx",
    "CBF #232_ Oct. 15, 1948.docx",
    "CBF #233_ Oct. 18, 1948.docx",
    "CBF #234_ Oct. 19, 1948.docx",
    "CBF #235_ Oct. 20, 1948.docx",
    "CBF #236_ Oct. 21, 1948.docx",
    "CBF #237_ Oct. 22, 1948.docx",
    "CBF #238_ Oct. 25, 1948.docx",
    "CBF #239_ Oct. 26, 1948.docx",
    "CBF #240_ Oct. 27, 1948.docx",
    "CBF #241_ Oct. 28, 1948.docx",
    "CBF #242_ Oct. 29, 1948.docx",
    "CBF #243_ Nov. 1, 1948.docx",
    "CBF #244_ Nov. 2, 1948.docx",
    "CBF #245_ Nov. 3, 1948.docx",
    "CBF #246_ Nov. 4, 1948.docx",
    "CBF #247_ Nov. 5, 1948.docx",
    "CBF #248_ Nov. 8, 1948.docx",
    "CBF #249_ Nov. 9, 1948.docx",
    "CBF #250_ Nov. 10, 1948.docx",
    "CBF #251_ Nov. 11, 1948.docx",
    "CBF #252_ Nov. 12, 1948.docx",
    "CBF #253_ Nov. 15, 1948.docx",
    "CBF #254_ Nov. 16, 1948.docx",
    "CBF #255_ Nov. 17, 1948.docx",
    "CBF #256_ Nov. 18, 1948.docx",
    "CBF #257_ Nov. 19, 1948.docx",
    "CBF #258_ Nov. 22, 1948.docx",
    "CBF #259_ Nov. 23, 1948.docx",
    "CBF #260_ Nov. 24, 1948.docx",
    "CBF #261_ Nov. 25, 1948.docx",
    "CBF #262_ Nov. 26, 1948.docx",
    "CBF #263_ Nov. 29, 1948.docx",
    "CBF #264_ Nov. 30, 1948.docx",
    "CBF #265_ Dec. 1, 1948.docx",
    "CBF #266_ Dec. 2, 1948.docx",
    "CBF #267_ Dec. 3, 1948.docx",
    "CBF #268_ Dec. 6, 1948.docx",
    "CBF #269_ Dec. 7, 1948.docx",
    "CBF #270_ Dec. 8, 1948.docx",
    "CBF #271_ Dec. 9, 1948.docx",
    "CBF #272_ Dec. 10, 1948.docx",
    "CBF #273_ Dec. 13, 1948.docx",
    "CBF #274_ Dec. 14, 1948.docx",
    "CBF #275_ Dec. 15, 1948.docx",
    "CBF #276_ Dec. 16, 1948.docx",
    "CBF #277_ Dec. 17, 1948.docx",
    "CBF #278_ Dec. 20, 1948.docx",
    "CBF #279_ Dec. 21, 1948.docx",
    "CBF #280_ Dec. 22, 1948.docx",
    "CBF #281_ Dec. 23, 1948.docx",
    "CBF #282_ Dec. 24, 1948.docx",
    "CBF #283_ Dec. 27, 1948.docx",
    "CBF #284_ Dec. 28, 1948.docx",
    "CBF #285_ Dec. 29, 1948.docx",
    "CBF #286_ Dec. 30, 1948.docx",
    "CBF #287_ Dec. 31, 1948.docx",
    "CBF #288_ Jan. 3, 1949.docx",
    "CBF #289_ Jan. 4, 1949.docx",
    "CBF #290_ Jan. 5, 1949.docx",
    "CBF #291_ Jan. 6, 1949.docx",
    "CBF #292_ Jan. 7, 1949.docx",
    "CBF #293_ Jan. 10, 1949.docx",
    "CBF #294_ Jan. 11, 1949.docx",
    "CBF #295_ Jan. 12, 1949.docx",
    "CBF #296_ Jan. 13, 1949.docx",
    "CBF #297_ Jan. 14, 1949.docx",
    "CBF #298_ Jan. 17, 1949.docx",
    "CBF #299_ Jan. 18, 1949.docx",
    "CBF #300_ Jan. 19, 1949.docx",
    "CBF #301_ Jan. 20, 1949.docx",
    "CBF #302_ Jan. 21, 1949.docx",
    "CBF #303_ Jan. 24, 1949.docx",
    "CBF #304_ Jan. 25, 1949.docx",
    "CBF #305_ Jan. 26, 1949.docx",
    "CBF #306_ Jan. 27, 1949.docx",
    "CBF #307_ Jan 28, 1949.docx",
    "CBF #308_ Jan. 31, 1949.docx",
    "CBF #309_ Feb. 1, 1949.docx",
    "CBF #310_ Feb. 2, 1949.docx",
    "CBF #311_ Feb. 3, 1949.docx",
    "CBF #312_ Feb. 4, 1949.docx",
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
