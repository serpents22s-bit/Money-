import requests
import time
from flask import Flask
from threading import Thread

# سيرفر الوهمي لبقاء الخدمة تعمل على Render
app = Flask('')
@app.route('/')
def home():
    return "سيرفر الأتمتة يعمل ويقوم بفحص البروكسيات..."

def run_server():
    app.run(host='0.0.0.0', port=8080)

# موديول سحب وفحص البروكسيات (المرحلة 1 في الفيديو)
def fetch_and_check_proxies():
    print("=== بدء تشغيل موديول البروكسيات التلقائي ===")
    
    # روابط جلب البروكسيات المجانية
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    
    while True:
        try:
            print("جاري سحب قوائم البروكسي من الإنترنت...")
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                proxies_list = response.text.splitlines()
                print(f"تم جلب {len(proxies_list)} بروكسي محتمل. جاري الفحص...")
                
                # فحص أول 10 بروكسيات كمرحلة تجريبية لتسريع السيرفر
                working_proxies = []
                for proxy in proxies_list[:10]:
                    try:
                        # فحص البروكسي عبر موقع جوجل كمعيار سرعة
                        test_proxy = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                        check = requests.get("https://www.google.com", proxies=test_proxy, timeout=3)
                        if check.status_code == 200:
                            print(f"✓ بروكسي يعمل وسريع: {proxy}")
                            working_proxies.append(proxy)
                    except:
                        continue
                
                # حفظ البروكسيات الشغالة في ملف نصي ليستدعيها بوت الحسابات لاحقاً
                with open("working_proxies.txt", "w") as f:
                    for wp in working_proxies:
                        f.write(f"{wp}\n")
                print("... تم تحديث المخزن بنجاح. البوت ينام لمدة 20 دقيقة الآن ...")
            else:
                print("فشل في جلب البروكسيات، المحاولة القادمة بعد قليل...")
        except Exception as e:
            print(f"خطأ في السيستم: {e}")
            
        time.sleep(1200) # ينام 20 دقيقة قبل الجولة التالية

if __name__ == "__main__":
    # تشغيل السيرفر في الخلفية
    t = Thread(target=run_server)
    t.start()
    
    # تشغيل الموديول الأساسي
    fetch_and_check_proxies()
    
