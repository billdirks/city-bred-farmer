# Path to files
path = "../../RawDocx/20250517/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #510601; June 1, 1951.docx",
    "CBF #510604; June 4, 1951.docx",
    "CBF #510605; June 5, 1951.docx",
    "CBF #510606; June 6, 1951.docx",
    "CBF #510607; June 7, 1951.docx",
    "CBF #510608; June 8, 1951.docx",
    "CBF #510611; June 11, 1951.docx",
    "CBF #510612; June 12, 1951.docx",
    "CBF #510613; June 13, 1951.docx",
    "CBF #510614; June 14, 1951.docx",
    "CBF #510615; June 15, 1951.docx",
    "CBF #510618; June 18, 1951.docx",
    "CBF #510619; June 19, 1951.docx",
    "CBF #510620; June 20, 1951.docx",
    "CBF #510621; June 21, 1951.docx",
    "CBF #510622; June 22, 1951.docx",
    "CBF #510625; June 25, 1951.docx",
    "CBF #510626; June 26, 1951.docx",
    "CBF #510627; June 27, 1951.docx",
    "CBF #510628; June 28, 1951.docx",
    "CBF #510629; June 29, 1951.docx",
    "CBF #520421; April 21, 1952.docx",
    "CBF #520801; Aug. 1, 1952.docx",
    "CBF #520804; Aug. 4, 1952.docx",
    "CBF #520805; Aug. 5, 1952.docx",
    "CBF #520806; Aug. 6, 1952.docx",
    "CBF #520807; Aug. 7, 1952.docx",
    "CBF #520808; Aug. 8, 1952.docx",
    "CBF #520811; Aug. 11, 1952.docx",
    "CBF #520812; Aug. 12, 1952.docx",
    "CBF #520813; Aug. 13, 1952.docx",
    "CBF #520814; Aug. 14, 1952.docx",
    "CBF #520815; Aug. 15, 1952.docx",
    "CBF #520818; Aug. 18, 1952.docx",
    "CBF #520819; Aug. 19, 1952.docx",
    "CBF #520820; Aug. 20, 1952.docx",
    "CBF #520822; Aug. 22, 1952.docx",
    "CBF #520825; Aug. 25, 1952.docx",
    "CBF #520826; Aug. 26, 1952.docx",
    "CBF #520827; Aug. 27, 1952.docx",
    "CBF #520828; Aug. 28, 1952.docx",
    "CBF #520829; Aug. 29, 1952.docx",
    "CBF #5208721; Aug. 21, 1952.docx",
    "CBF #531002; Oct. 2, 1953.docx",
    "CBF #531005; Oct. 5, 1953.docx",
    "CBF #531009; Oct. 9, 1953.docx",
    "CBF #531012; Oct. 12, 1953.docx",
    "CBF #531016; Oct. 16, 1953.docx",
    "CBF #531021; Oct. 21, 1953.docx",
    "CBF #531023; Oct. 23, 1953.docx",
    "CBF #531026; Oct. 26, 1953.docx",
    "CBF #531028; Oct. 28, 1953.docx",
    "CBF #531030; Oct. 30, 1953.docx",
    "CBF #541208; Dec. 8, 1954.docx",
    "CBF #541215; Dec. 15, 1954.docx",
    "CBF #751; Oct. 11, 1950.docx",
    "CBF #752; Oct. 12, 1950.docx",
    "CBF #753; Oct. 13, 1950.docx",
    "CBF #754; Oct. 16, 1950.docx",
    "CBF #755; Oct. 17, 1950.docx",
    "CBF #756; Oct. 18, 1950.docx",
    "CBF #757; Oct. 19, 1950.docx",
    "CBF #758; Oct. 20, 1950.docx",
    "CBF #759; Oct. 23, 1950.docx",
    "CBF #760; Oct. 24, 1950.docx",
    "CBF #761; Oct. 25, 1950.docx",
    "CBF #762; Oct. 26, 1950.docx",
    "CBF #764; Oct. 30, 1950.docx",
    "CBF #765; Oct. 31, 1950.docx",
    "CBF #766; Nov. 1, 1950.docx",
    "CBF #767; Nov. 2, 1950.docx",
    "CBF #768; Nov. 3, 1950.docx",
    "CBF #769; Nov. 6, 1950.docx",
    "CBF #770; Nov. 7, 1950.docx",
    "CBF #772; Nov. 9, 1950.docx",
    "CBF #773; Nov. 10, 1950.docx",
    "CBF #774; Nov. 13, 1950.docx",
    "CBF #775; Nov. 14, 1950.docx",
    "CBF #777; Nov. 16, 1950.docx",
    "CBF #778; Nov. 17, 1950.docx",
    "CBF #779; Nov. 20, 1950.docx",
    "CBF #780; Nov. 21, 1950.docx",
    "CBF #781; Nov. 22, 1950.docx",
    "CBF #784; Nov. 27; 1950.docx",
    "CBF #786; Nov. 29, 1950.docx",
    "CBF #787; Nov. 30, 1950.docx",
    "CBF #788; Dec. 1, 1950.docx",
    "CBF #789; Dec. 4, 1950.docx",
    "CBF #791; Dec. 6, 1950.docx",
    "CBF #792; Dec. 7, 1950.docx",
    "CBF #793; Dec. 8, 1950.docx",
    "CBF #794; Dec. 11, 1950.docx",
    "CBF #795; Dec. 12, 1950.docx",
    "CBF #796; Dec. 13, 1950.docx",
    "CBF #797; Dec. 14, 1950.docx",
    "CBF #798; Dec. 15, 1950.docx",
    "CBF #799; Dec. 18, 1950.docx",
    "CBF #800; Dec. 19, 1950.docx",
    "CBF #801; Dec. 20, 1950.docx",
    "CBF #802; Dec. 21, 1950.docx",
    "CBF #803; Dec. 22, 1950.docx",
    "CBF #804; Dec. 25, 1950.docx",
    "CBF #805; Dec. 26, 1950.docx",
    "CBF #806; Dec. 27, 1950.docx",
    "CBF #807; Dec. 28, 1950.docx",
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
