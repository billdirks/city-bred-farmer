# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"; done | xargs -0
files = [
    "CBF #10_ July 8, 1946.docx",
    "CBF #11_ July 15, 1946.docx",
    "CBF #12_ July 22, 1946.docx",
    "CBF #13_ July 29, 1946.docx",
    "CBF #14_ August 5, 1946.docx",
    "CBF #15_ August 12, 1946.docx",
    "CBF #16_ August 19, 1946.docx",
    "CBF #17_ August 26, 1946.docx",
    "CBF #18_ Sept. 2, 1946.docx",
    "CBF #19_ Sept. 9, 1946.docx",
    "CBF #1_ May 7, 1946.docx",
    "CBF #20_ Sept. 16, 1946.docx",
    "CBF #21_ Sept 23, 1946.docx",
    "CBF #22_ Sept. 30, 1946.docx",
    "CBF #23_ Oct. 7, 1946.docx",
    "CBF #24_ Oct. 14, 1946.docx",
    "CBF #25_ Oct. 21, 1946.docx",
    "CBF #26_ Oct. 28, 1946.docx",
    "CBF #27_ Nov. 4, 1946.docx",
    "CBF #28_ Nov. 11, 1946.docx",
    "CBF #29_ Nov. 18, 1946.docx",
    "CBF #2_ May 13, 1946.docx",
    "CBF #31_ Dec. 2, 1946.docx",
    "CBF #32_ Dec. 9, 1946.docx",
    "CBF #33_ Dec. 16, 1946.docx",
    "CBF #34_ Dec. 23, 1946.docx",
    "CBF #35_ Dec. 30, 1946.docx",
    "CBF #36_ Jan. 6, 1947.docx",
    "CBF #37_ Jan. 13, 1947.docx",
    "CBF #38_ Jan. 20, 1947.docx",
    "CBF #39_ Jan. 27, 1947.docx",
    "CBF #3_ May 20, 1946.docx",
    "CBF #40_ Feb. 3, 1947.docx",
    "CBF #41_ Feb. 10, 1947.docx",
    "CBF #42_ Feb. 17, 1947.docx",
    "CBF #43_ Feb. 24, 1947.docx",
    "CBF #4_ May 27, 1946.docx",
    "CBF #5_ June 3, 1946.docx",
    "CBF #6_ June 10, 1946.docx",
    "CBF #7_ June 17, 1946.docx",
    "CBF #8_ June 24, 1946.docx",
    "CBF #9_ July 1, 1946.docx",
    "CBF_ Nov. 25, 1946.docx",
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
        print(f'python3 ./ingest_docx.py --date {year}{month}{day} --docx "../../RawDocx/{f}"')
