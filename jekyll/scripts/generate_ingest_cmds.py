# Path to files
path = "../../RawDocx/20250405/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #549; Jan. 2, 1950.docx",
    "CBF #550; Jan. 3, 1950.docx",
    "CBF #551; Jan. 4, 1950.docx",
    "CBF #552; Jan. 5, 1950.docx",
    "CBF #553; Jan. 6, 1950.docx",
    "CBF #554; Jan. 9, 1950.docx",
    "CBF #555; Jan. 10, 1950.docx",
    "CBF #556; Jan. 11, 1950.docx",
    "CBF #557; Jan. 12, 1950.docx",
    "CBF #558; Jan. 13, 1950.docx",
    "CBF #559; Jan. 16, 1950.docx",
    "CBF #560; Jan. 17, 1950.docx",
    "CBF #561; Jan. 18, 1950.docx",
    "CBF #562; Jan. 19, 1950.docx",
    "CBF #563; Jan. 20, 1950.docx",
    "CBF #564; Jan. 23, 1950.docx",
    "CBF #565; Jan. 24, 1950.docx",
    "CBF #566; Jan. 25, 1950.docx",
    "CBF #567; Jan. 26, 1950.docx",
    "CBF #568; Jan. 27, 1950.docx",
    "CBF #569; Jan. 30, 1950.docx",
    "CBF #570; Jan. 31, 1950.docx",
    "CBF #571; Feb. 1, 1950.docx",
    "CBF #572; Feb. 2, 1950.docx",
    "CBF #573; Feb. 3, 1950.docx",
    "CBF #574; Feb. 6, 1950.docx",
    "CBF #575; Feb. 7, 1950.docx",
    "CBF #576; Feb. 8, 1950.docx",
    "CBF #577; Feb. 9, 1950.docx",
    "CBF #578; Feb. 10, 1950.docx",
    "CBF #579; Feb. 13, 1950.docx",
    "CBF #580; Feb. 14, 1950.docx",
    "CBF #581; Feb. 15, 1950.docx",
    "CBF #582; Feb. 16, 1950.docx",
    "CBF #583; Feb. 17, 1950.docx",
    "CBF #584; Feb. 20, 1950.docx",
    "CBF #585; Feb. 21, 1950.docx",
    "CBF #586; Feb. 22, 1950.docx",
    "CBF #587; Feb. 23, 1950.docx",
    "CBF #588; Feb. 24, 1950.docx",
    "CBF #589; Feb. 27, 1950.docx",
    "CBF #590; Feb. 28, 1950.docx",
    "CBF #591; March 1, 1950.docx",
    "CBF #592; March 2, 1950.docx",
    "CBF #593; March 3, 1950.docx",
    "CBF #594; March 6, 1950.docx",
    "CBF #595; March 7, 1950.docx",
    "CBF #596; March 8, 1950.docx",
    "CBF #597; March 9, 1950.docx",
    "CBF #598; March 10, 1950.docx",
    "CBF #599; March 13, 1950.docx",
    "CBF #600; March 14, 1950.docx",
    "CBF #601; March 15, 1950.docx",
    "CBF #602; March 16, 1950.docx",
    "CBF #603; March 17, 1950.docx",
    "CBF #604; March 20, 1950.docx",
    "CBF #605; March 21, 1950.docx",
    "CBF #606; March 22, 1950.docx",
    "CBF #607; March 23, 1950.docx",
    "CBF #608; March 24, 1950.docx",
    "CBF #609; March 27, 1950.docx",
    "CBF #610; March 28, 1950.docx",
    "CBF #611; March 29, 1950.docx",
    "CBF #612; March 30, 1950.docx",
    "CBF #613; March 31, 1950.docx",
    "CBF #614; April 3, 1950.docx",
    "CBF #615; April 4, 1950.docx",
    "CBF #616; April 5, 1950.docx",
    "CBF #617; April 6, 1950.docx",
    "CBF #618; April 7, 1950.docx",
    "CBF #619; April 10, 1950.docx",
    "CBF #620; April 11, 1950.docx",
    "CBF #621; April 12, 1950.docx",
    "CBF #622; April 13, 1950.docx",
    "CBF #623; April 14, 1950.docx",
    "CBF #624; April 17, 1950.docx",
    "CBF #625; April 18, 1950.docx",
    "CBF #626; April 19, 1950.docx",
    "CBF #627; April 20, 1950.docx",
    "CBF #628; April 21, 1950.docx",
    "CBF #629; April 24, 1950.docx",
    "CBF #630; April 25, 1950.docx",
    "CBF #631; April 26, 1950.docx",
    "CBF #632; April 27, 1950.docx",
    "CBF #633; April 28, 1950.docx",
    "CBF #634; May 1, 1950.docx",
    "CBF #635; May 2, 1950.docx",
    "CBF #636; May 3, 1950.docx",
    "CBF #637; May 4, 1950.docx",
    "CBF #638; May 5, 1950.docx",
    "CBF #639; May 8, 1950.docx",
    "CBF #640; May 9, 1950.docx",
    "CBF #641; May 10, 1950.docx",
    "CBF #642; May 11, 1950.docx",
    "CBF #643; May 12, 1950.docx",
    "CBF #644; May 15, 1950.docx",
    "CBF #645; May 16, 1950.docx",
    "CBF #646; May 17, 1950.docx",
    "CBF #647; May 18, 1950.docx",
    "CBF #648, May 19, 1950.docx",
    "CBF #649; May 22, 1950.docx",
    "CBF #650; May 23, 1950.docx",
    "CBF #651; May 24, 1950.docx",
    "CBF #652; May 25, 1950.docx",
    "CBF #654; May 29, 1950.docx",
    "CBF #655; May 30, 1950.docx",
    "CBF #656; May 31, 1950.docx",
    "CBF #657; June 1, 1950.docx",
    "CBF #658; June 2, 1950.docx",
    "CBF #659; June 5, 1950.docx",
    "CBF #660; June 6, 1950.docx",
    "CBF #661; June 7, 1950.docx",
    "CBF #662; June 8, 1950.docx",
    "CBF #663; June 9, 1950.docx",
    "CBF #664; June 12, 1950.docx",
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
