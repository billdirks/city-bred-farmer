# Path to files
path = "../../RawDocx/20250427/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #665; June 13, 1950.docx",
    "CBF #666; June 14, 1950.docx",
    "CBF #667; June 15, 1950.docx",
    "CBF #668; June 16, 1950.docx",
    "CBF #669; June 19, 1950.docx",
    "CBF #670; June 20, 1950.docx",
    "CBF #671; June 21, 1950.docx",
    "CBF #672; June 22, 1950.docx",
    "CBF #673; June 23, 1950.docx",
    "CBF #674; June 26, 1950.docx",
    "CBF #675; June 27, 1950.docx",
    "CBF #676; June 28, 1950.docx",
    "CBF #677; June 29, 1950.docx",
    "CBF #678; June 30, 1950.docx",
    "CBF #679; July 3, 1950.docx",
    "CBF #680; July 4, 1950.docx",
    "CBF #681; July 5, 1950.docx",
    "CBF #682; July 6, 1950.docx",
    "CBF #683; July 7, 1950.docx",
    "CBF #684; July 10, 1950.docx",
    "CBF #685; July 11, 1950.docx",
    "CBF #686; July 12, 1950.docx",
    "CBF #687; July 13, 1950.docx",
    "CBF #688; July 14, 1950.docx",
    "CBF #689; July 17, 1950.docx",
    "CBF #690; July 18, 1950.docx",
    "CBF #691; July 19, 1950.docx",
    "CBF #692; July 20, 1950.docx",
    "CBF #693; July 21, 1950.docx",
    "CBF #694; July 24, 1950.docx",
    "CBF #695; July 25, 1950.docx",
    "CBF #696; July 26, 1950.docx",
    "CBF #697; July 27, 1950.docx",
    "CBF #698; July 28, 1950.docx",
    "CBF #699; July 31, 1950.docx",
    "CBF #700; Aug. 1, 1950.docx",
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
