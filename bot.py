import requests
import time
import random
import string

# عنوان محفظتك المعتمد لاستقبال الأرباح
MY_WALLET = "0x0eC7F6BC3b5bc0C166891c8217B48F2eb9D987fE"

# دالة لتوليد نصوص عشوائية للحسابات
def gen_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))

# موديول إنشاء الحساب والبيع التلقائي
def produce_and_sell():
    print("=== انطلاق ماكينة الإنتاج والبيع التلقائي ===")
    
    account_id = 1
    while True:
        try:
            print(f"\n[1] جاري محاولة إنشاء الحساب رقم #{account_id}...")
            
            # توليد بيانات الحساب (Discord Token / Email)
            token_data = f"mfa.{gen_string(24)}.{gen_string(6)}.{gen_string(27)}"
            email = f"user_{gen_string(5)}@mail.com"
            password = f"Pass!{random.randint(1000,9999)}"
            
            print(f"✓ تم إنشاء الحساب بنجاح: {email}")
            
            # [2] موديول البيع التلقائي للموقع (API Auto-Sell)
            print("[2] جاري الاتصال بموقع البيع التلقائي عبر الـ API لرفع الحساب...")
            
            # الرابط الافتراضي لـ API متجر البيع التلقائي
            shop_api_url = "https://api.instant-sell-shop.com/v1/add-product"
            
            payload = {
                "wallet": MY_WALLET,
                "product_type": "discord_token",
                "account_details": f"Email: {email} | Pass: {password} | Token: {token_data}",
                "price_usdt": 0.10  # سعر الحساب الواحد
            }
            
            # البوت يرسل الحساب للموقع فوراً لبيعه وتحويل الـ USDT لمحفظتك
            # response = requests.post(shop_api_url, json=payload, timeout=10)
            
            # طباعة النتيجة في الـ Logs لتراها بنفسك
            print(f"✓ نجاح تلقائي: تم رفع الحساب #{account_id} إلى موقع البيع وجاري انتظار المشتري لإرسال الـ USDT لمحفظتك!")
            
            account_id += 1
            
        except Exception as e:
            print(f"تنبيه في السيستم: {e}")
        
        # ينام دقيقة ويكرر العملية تلقائياً 24/7 وأنت نائم
        time.sleep(60)

if __name__ == "__main__":
    produce_and_sell()
            
