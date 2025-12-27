data = """1984,SciFi,35,0.25
The Hobbit,Fantasy,5,0.50
Calculus,Textbook,45,1.00
Dune,SciFi,10,0.25
Mistborn,Fantasy,12,0.50
Broken,Line,Here
Physics,Textbook,2,1.00
Harry Potter,Fantasy,3,0.50"""

with open('overdue_log.txt', 'w') as file:
    file.write(data)

def analyze_fines(filename):
    genre_totals = {}
    severe_books = []
    with open(filename, 'r') as f:
        for line in f:
            line_list = line.strip().split(",")
            if len(line_list) != 4:
                continue
            try:
                name = line_list[0]
                genre = line_list[1]
                DaysOverdue = int(line_list[2])
                FinePerDay = float(line_list[3])
            except ValueError:
                continue  
            TotalFine = DaysOverdue * FinePerDay
            if genre in genre_totals:
                genre_totals[genre] += TotalFine
            else:
                genre_totals[genre] = TotalFine
            
            if DaysOverdue > 30:
                severe_books.append((name, DaysOverdue))
    return genre_totals, severe_books

def save_fine_report(genre_totals, severe_books):
    with open('fine_report.txt', 'w') as file:
        file.write("GENRE FINE REVENUE\n")
        file.write("------------------\n")
        for genre, total in genre_totals.items():
            file.write(f"{genre}: ${total}\n")
        file.write("\n")
        file.write("SEVERE DELAYS (> 30 Days)\n")
        file.write("-------------------------\n")
        for i in severe_books:
            file.write(f"{i[0]} ({i[1]} days)\n")

genre_totals, severe_books = analyze_fines("overdue_log.txt")
save_fine_report(genre_totals, severe_books)
