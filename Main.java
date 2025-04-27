import java.util.Scanner;
class Library {
    String[] books;
    int No_of_Books;

    Library() {
        this.books = new String[100];
        this.No_of_Books = 0;
    }

    void addBook(String book) {
        this.books[No_of_Books] = book;
        No_of_Books++;
        System.out.println(book + " has been added");
    }

    void show_Available_Books() {
        System.out.println("Available books are:");
        for (String book : this.books) {
            if (book == null) {
                continue;
            }
            System.out.println("*" + book);
        }
    }

    void issueBook(String book) {
        for (String b : this.books) {
            for (int i = 0; i < this.books.length; i++) {
                if (this.books[i].equals(book)) {
                    System.out.println("The book has been issued");
                    this.books[i] = null;
                    return;
                }
                System.out.println("*" + book);
            }
            System.out.println("This book does not exist");
        }
    }
        void returnBook(String book){
            addBook(book);
            System.out.println("Returned "+book);
        }
    }
    class Main {
        public static void main(String[] args) {
            Library l = new Library();
            l.addBook("Java Fundamentals");
            l.addBook("Algorithm Design");
            l.addBook("11 truths of Life");
            l.addBook("Think and grow rich");
            l.show_Available_Books();
            l.issueBook("Java Fundamentals");
            l.show_Available_Books();//since java book is issued it does not show in
            // the list of books as we have used continue statement
            l.returnBook("Java Fundamentals");
            l.show_Available_Books();
        }
    }
