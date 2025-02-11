# Path to files
path = "../../RawDocx/20250210/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #129_ June 1, 1948.docx",
    "CBF #130_ June 2, 1948.docx",
    "CBF #131_ June 3, 1948.docx",
    "CBF #132_ June 4, 1948.docx",
    "CBF #133_ June 7, 1948.docx",
    "CBF #134_ June 8, 1948.docx",
    "CBF #135_ June 9, 1948.docx",
    "CBF #136_ June 10, 1948.docx",
    "CBF #137_ June 11, 1948.docx",
    "CBF #138_ June 14, 1948.docx",
    "CBF #139, June 15, 1948.docx",
    "CBF #140_ June 16, 1948.docx",
    "CBF #141_ June 17, 1948.docx",
    "CBF #142_ June 21, 1948.docx",
    "CBF #143_ June 22, 1948.docx",
    "CBF #144_ June 23, 1948.docx",
    "CBF #145_ June 24, 1948.docx",
    "CBF #146_ June 25, 1948.docx",
    "CBF #147_ June 28, 1948.docx",
    "CBF #148_ June 29, 1948.docx",
    "CBF #149_ June 30, 1948.docx",
    "CBF #150_ July 1, 1948.docx",
    "CBF #151_ July 2, 1948.docx",
    "CBF #152_ July 5, 1948.docx",
    "CBF #153_ July 6, 1948.docx",
    "CBF #154_ July 7, 1948.docx",
    "CBF #155_ July 8, 1948.docx",
    "CBF #156_ July 9, 1948.docx",
    "CBF #157_ July 12, 1948.docx",
    "CBF #158_ July 13, 1948.docx",
    "CBF #159_ July 14, 1948.docx",
    "CBF #160_ July 15, 1948.docx",
    "CBF #161_ July 16, 1948.docx",
    "CBF #162_ July 19, 1948.docx",
    "CBF #163_ July 20, 1948.docx",
    "CBF #164_ July 21, 1948.docx",
    "CBF #165_ July 22, 1948.docx",
    "CBF #166_ July 23, 1948.docx",
    "CBF #167_ July 26, 1948.docx",
    "CBF #168_ July 27, 1948.docx",
    "CBF #169_ July 28, 1948.docx",
    "CBF #170_ July 29, 1948.docx",
    "CBF #171_ July 30, 1948.docx",
    "CBF #172_ Aug. 2, 1948.docx",
    "CBF #173_ Aug. 3, 1948.docx",
    "CBF #174_ Aug. 4, 1948.docx",
    "CBF #175_ Aug. 5, 1948.docx",
    "CBF #176_ Aug. 6, 1948.docx",
    "CBF #177_ Aug. 9, 1948.docx",
    "CBF #178_ Aug. 10, 1948.docx",
    "CBF #179_ Aug. 11, 1948.docx",
    "CBF #180_ Aug. 12, 1948.docx",
    "CBF #181_ Aug. 13, 1948.docx",
    "CBF #182_ Aug. 16, 1948.docx",
    "CBF #183_ Aug. 17, 1948.docx",
    "CBF #184_ Aug. 18, 1948.docx",
    "CBF #185_ Aug. 19, 1948.docx",
    "CBF #186_ Aug. 20, 1948.docx",
    "CBF #187_ Aug. 23, 1948.docx",
    "CBF #188_ Aug. 24, 1948.docx",
    "CBF #189_ Aug. 25, 1948.docx",
    "CBF #190_ Aug. 26, 1948.docx",
    "CBF #191_ Aug. 27, 1948.docx",
    "CBF #192_ Aug. 30, 1948.docx",
    "CBF #193_ Aug. 31, 1948.docx",
    "CBF #194_ Sept. 1, 1948.docx",
    "CBF #195_ Sept. 2, 1948.docx",
    "CBF #196_ Sept. 3, 1948.docx",
    "CBF #197_ Sept. 4, 1948.docx",
    "CBF #198_ Sept. 6, 1948.docx",
    "CBF #199_ Sept. 7, 1948.docx",
    "CBF #200_ Sept. 8, 1948.docx",
    "CBF #201_ Sept. 9, 1948.docx",
    "CBF #202_ Sept. 10, 1948.docx",
    "CBF #203_ Sept. 11, 1948.docx",
    "CBF #204_ Sept. 13, 1948.docx",
    "CBF #205_ Sept. 14, 1948.docx",
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
