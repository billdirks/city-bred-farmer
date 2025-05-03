# Path to files
path = "../../RawDocx/20250503/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #701; Aug. 2, 1950.docx",
    "CBF #702; Aug. 3, 1950.docx",
    "CBF #703; Aug. 4, 1950.docx",
    "CBF #704; Aug. 7, 1950.docx",
    "CBF #705; Aug. 8, 1950.docx",
    "CBF #706; Aug. 9, 1950.docx",
    "CBF #707; Aug. 10, 1950.docx",
    "CBF #708; Aug. 11, 1950.docx",
    "CBF #709; Aug. 14, 1950.docx",
    "CBF #710; Aug. 15, 1950.docx",
    "CBF #711; Aug. 16, 1950.docx",
    "CBF #712; Aug. 17, 1950.docx",
    "CBF #713; Aug. 18, 1950.docx",
    "CBF #714; Aug. 21, 1950.docx",
    "CBF #715; Aug. 22, 1950.docx",
    "CBF #716; Aug. 23, 1950.docx",
    "CBF #717; Aug. 24, 1950.docx",
    "CBF #718; Aug. 25, 1950.docx",
    "CBF #719; Aug. 28, 1950.docx",
    "CBF #720; Aug. 29, 1950.docx",
    "CBF #721; Aug. 30, 1950.docx",
    "CBF #722; Aug. 31, 1950.docx",
    "CBF #723; Sept. 1, 1950.docx",
    "CBF #724; Sept. 4, 1950.docx",
    "CBF #725_ Sept. 5, 1950.docx",
    "CBF #726; Sept. 6, 1950.docx",
    "CBF #727; Sept. 7, 1950.docx",
    "CBF #728; Sept. 8, 1950.docx",
    "CBF #729; Sept. 11, 1950.docx",
    "CBF #730; Sept. 12, 1950.docx",
    "CBF #731; Sept. 13, 1950.docx",
    "CBF #732; Sept. 14, 1950.docx",
    "CBF #733; Sept. 15, 1950.docx",
    "CBF #734; Sept. 18, 1950.docx",
    "CBF #735; Sept. 19, 1950.docx",
    "CBF #736; Sept. 20, 1950.docx",
    "CBF #737; Sept. 21, 1950.docx",
    "CBF #738; Sept. 22, 1950.docx",
    "CBF #739; Sept. 25, 1950.docx",
    "CBF #740; Sept. 26, 1950.docx",
    "CBF #741; Sept. 27, 1950.docx",
    "CBF #742; Sept. 28, 1950.docx",
    "CBF #743; Sept. 29, 1950.docx",
    "CBF #744; Oct. 2, 1950.docx",
    "CBF #745; Oct. 3, 1950.docx",
    "CBF #746; Oct. 4, 1950.docx",
    "CBF #747; Oct. 5, 1950.docx",
    "CBF #749; Oct. 9, 1950.docx",
    "CBF #750; Oct. 10, 1950.docx",
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
