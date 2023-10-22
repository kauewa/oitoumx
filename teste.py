from pdfminer.high_level import extract_text

import requests

def fetch_pdf_content(url):
    response = requests.get(url)
    return response.text

def extract_pdf_content(pdf_path):
    return extract_text(pdf_path)

if __name__ == "__main__":
    pdf_url = "https://results.supermotocross.com/xml/SX/events/S2305/S2F1PRESS.pdf"
    pdf = fetch_pdf_content(pdf_url)
    content = extract_pdf_content(pdf)
    print(content)


# def parse_pdf_content(content):
#     lines = content.split("\n")
#     results = []
#     for line in lines:
#         if line.startswith("#"):
#             data = line.split()
#             rider = {
#                 "Number": data[0],
#                 "Name": " ".join(data[1:-6]),
#                 "Bike": data[-6],
#                 "Start Position": data[-5],
#                 "Finish": data[-4],
#                 "Points": data[-3],
#                 "Holeshot": data[-2],
#                 "Qual": data[-1]
#             }
#             results.append(rider)
#     return results

# def main():
#     url = "https://results.supermotocross.com/xml/SX/events/S2305/S2F1PRESS.pdf"
#     content = fetch_pdf_content(url)
#     print(content)
#     # race_results = parse_pdf_content(content)
#     # return race_results

# if __name__ == "__main__":
#     results = main()
#     # for rider in results:
#     #     print(rider)

