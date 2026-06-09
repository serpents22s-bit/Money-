import time
import random

def start_account_farm():
    print("=== انطلاق مزرعة الحسابات التلقائية المستقرة ===")
    my_wallet = "0x0eC7F6BC3b5bc0C166891c8217B48F2eb9D987fE"
    account_id = 1

    while True:
        try:
            print(f"[جاري العمل] محاولة إنشاء الحساب رقم #{account_id}...")
            
            # توليد بيانات حساب عشوائية ومؤمنة
            username = f"user_bep20_{random.randint(1000, 9999)}"
            password = f"Pass_{random.randint(10000, 99999)}"
            email = f"{username}@mail-farm.com"
            
            # حفظ بيانات الحساب في ملف نصي على السيرفر
            with open("generated_accounts.txt", "a") as f:
                f.write(f"Email: {email} | Pass: {password} | Wallet: {my_wallet}\n")
            
            print(f"✓ نجاح: تم توليد وتخزين الحساب #{account_id}")
            account_id += 1
            
        except Exception as e:
            print(f"تنبيه في السيستم: {e}")
        
        # الانتظار لمدة دقيقة واحدة قبل توليد الحساب التالي
        time.sleep(60)

if __name__ == "__main__":
    start_account_farm()
    
