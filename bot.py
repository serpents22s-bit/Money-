import requests
import time
import random
from flask import Flask
from threading import Thread

# سيرفر البقاء مستيقظاً لـ Render
app = Flask('')
@app.route('/')
def home():
    return "مزرعة الأتمتة تعمل وتولد الحسابات الآن!"

def run_server():
    app.run(host='0.0.0.0', port=8080)

# موديول توليد الحسابات التلقائي (المرحلة 2)
def start_account_farm():
    print("=== انطلاق مزرعة الحسابات التلقائية ===")
    my_wallet = "0x0eC7F6BC3b5bc0C166891c8217B48F2eb9D987fE"
    account_id = 1

    while True:
        try:
            # محاكاة لعملية الاتصال وتوليد حساب ديسكورد/إيميل مؤمن
            print(f"[جاري العمل] محاولة إنشاء الحساب رقم #{account_id} عبر البروكسي المتاح...")
            
            # هنا السيرفر يقوم بإنشاء وتجهيز بيانات الحساب
            username = f"user_bep20_{random.randint(1000, 9999)}"
            password = f"Pass_{random.randint(10000, 99999)}"
            email = f"{username}@mail-farm.com"
            
            # حفظ الحساب الناتج فوراً في ملف البضاعة الرقمية
            with open("generated_accounts.txt", "a") as f:
                f.write(f"Email: {email} | Pass: {password} | Wallet_Linked: {my_wallet}\n")
            
            print(f"✓ نجاح: تم توليد الحساب #{account_id} وتخزينه في المخزن الرقمي.")
            account_id += 1
            
        except Exception as e:
            print(f"تنبيه في السيستم: {e}")
        
        # السيرفر يعمل وينتج حساباً جديداً كل دقيقتين بانتظام
        time.sleep(120)

if __name__ == "__main__":
    # تشغيل السيرفر الويب لحماية الخدمة من الإغلاق
    t = Thread(target=run_server)
    t.start()
    
    # بدء تشغيل المزرعة فوراً بدون تأخير البروكسيات
    start_account_farm()
    
