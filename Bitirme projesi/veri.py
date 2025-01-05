import sqlite3

# Veritabanına bağlan ve gerekli tabloları oluştur
def initialize_database():
    conn = sqlite3.connect('student_performance.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Exams (
            exam_id INTEGER PRIMARY KEY,
            exam_name TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Questions (
            question_id INTEGER PRIMARY KEY,
            exam_id INTEGER,
            subject TEXT,
            subtopic TEXT,
            FOREIGN KEY (exam_id) REFERENCES Exams(exam_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS StudentAnswers (
            answer_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            exam_id INTEGER,
            question_id INTEGER,
            is_correct INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (exam_id) REFERENCES Exams(exam_id),
            FOREIGN KEY (question_id) REFERENCES Questions(question_id)
        )
    ''')
    
    conn.commit()
    conn.close()

initialize_database()
