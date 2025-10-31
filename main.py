import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_word_typewriter(word, char_speed=1.3):
    """
    Print kata dengan efek typewriter (huruf per huruf)
    char_speed: kecepatan per huruf dalam detik
    """
    for char in word:
        print(char, end='', flush=True)
        time.sleep(char_speed)

def play_lyrics():
    """
    Main function - per kata muncul dengan efek typewriter
    Timing per kata mengikuti lagu asli
    """
    
    # Format: ('kata', char_speed, delay_setelah_kata)
    # char_speed: kecepatan typing per huruf (0.05-0.15 detik)
    # delay_setelah_kata: jeda sebelum kata berikutnya (detik)
    
    lyrics_words = [
        
        ("Don't", 0.08, 0.3),        
        ("make", 0.08, 0.2),
        ("me", 0.08, 0.3),
        ("close", 0.1, 1.3),
        ("one", 0.07, 0.1),
        ("more", 0.09, 0.08),
        ("door", 0.09, 0.8),         
        ("\n", 0, 0.08),             
        
        ("I", 0.06, 0.1),
        ("don't", 0.08, 0.1),
        ("wanna", 0.05, 0.09),
        ("hurt", 0.09, 1.0),
        ("anymore", 0.07, 1.0),      
        ("\n", 0, 0.010),
        
        ('Stay in',0.08,0.12),
        ('my arms',0.08,1.6),
        ('if',0.06,0.09),
        ('you',0.08,0.09),
        ('dare',0.09,0.6),
        ("\n", 0, 0.08),
        
        ('Or',0.04,0.09),
        ('must',0.09,0.1),
        ('I',1.0,0.09),
        ('imagine',0.20,0.15),
        ('you',0.09,0.09),
        ('there',0.09,0.10),
        ("\n", 0, 1.5),
        
        # ('Dont',00.8,0.1),
        # ('walk',0.1,0.1),
        # ('away',0.2,0.1),
        # ('from me',0.3,0.10),
        # ("\n", 0, 1.5),
        
        # ('I have',0.1,0.2),
        # ('nothing,',0.1,0.1),
        # ('nothing,',0.1,0.1),
        # ('nothing',0.1,0.10),
        # ("\n", 0, 1.5),
        
        # ('If',0.2,0.3),
        # ('I dont',0.1, 0.3),
        # ('have you',0.1,0.1),
        
    ]
    
    clear_screen()
    print('\n' + '='*70)
    print('🎵  I Have Nothing - Whitney Houston (Chorus)  🎵'.center(70))
    print('='*70 + '\n\n')
    time.sleep(1.5)  # Delay intro sebelum mulai
    
    for word, char_speed, delay_after in lyrics_words:
        
        if word == "\n":  # Baris baru
            print()
            time.sleep(delay_after)
            continue
        
        print_word_typewriter(word, char_speed)
        
        # Spasi setelah kata
        print(' ', end='', flush=True)
        
        # Delay sebelum kata berikutnya
        time.sleep(delay_after)
    
    # print('\n\n' + '='*70)
    # print('💫  End  💫'.center(70))
    # print('='*70 + '\n')

if __name__ == "__main__":

    play_lyrics()
