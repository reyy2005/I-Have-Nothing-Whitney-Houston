import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_word_typewriter(word, char_speed=0.08):
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
        # GANTI dengan lirik "I Have Nothing" chorus
        # Contoh timing:
        
        ("Don't", 0.08, 0.3),        # Huruf muncul cepat, delay 0.3s
        ("make", 0.08, 0.2),
        ("me", 0.08, 0.3),
        ("close", 0.08, 0.4),
        ("one", 0.08, 0.3),
        ("more", 0.08, 0.3),
        ("door", 0.10, 0.8),         # Huruf lebih slow, delay lebih lama
        ("\n", 0, 1.0),              # Baris baru dengan jeda
        
        ("I", 0.08, 0.2),
        ("don't", 0.08, 0.3),
        ("wanna", 0.08, 0.3),
        ("hurt", 0.08, 0.4),
        ("anymore", 0.10, 1.0),      # Kata panjang, slow typing
        ("\n", 0, 1.5),
        
        # Tambahkan lirik lengkap di sini...
    ]
    
    clear_screen()
    print('\n' + '='*70)
    print('🎵  I Have Nothing - Whitney Houston (Chorus)  🎵'.center(70))
    print('='*70 + '\n\n')
    time.sleep(3.0)  # Delay intro sebelum mulai
    
    for word, char_speed, delay_after in lyrics_words:
        
        if word == "\n":  # Baris baru
            print()
            time.sleep(delay_after)
            continue
        
        # Print kata dengan efek typewriter
        print_word_typewriter(word, char_speed)
        
        # Spasi setelah kata
        print(' ', end='', flush=True)
        
        # Delay sebelum kata berikutnya
        time.sleep(delay_after)
    
    print('\n\n' + '='*70)
    print('💫  End  💫'.center(70))
    print('='*70 + '\n')

if __name__ == "__main__":
    # Pilih versi yang Anda mau:
    
    # Versi simple (tanpa warna):
    play_lyrics()
    
    # Atau dengan warna:
    # play_lyrics_with_color()