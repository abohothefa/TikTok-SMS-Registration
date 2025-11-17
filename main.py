import os
from openai import OpenAI

# الحصول على مفتاح OpenAI من متغيرات البيئة
api_key = os.environ.get('openai')

if api_key:
    print('✓ تم العثور على مفتاح OpenAI')
    
    # إنشاء عميل OpenAI
    client = OpenAI(api_key=api_key)
    
    # مثال على استخدام API
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "مرحباً، كيف حالك؟"}
            ]
        )
        print(f"✓ استجابة من OpenAI: {response.choices[0].message.content}")
    except Exception as e:
        print(f"✗ خطأ في الاتصال: {e}")
else:
    print('✗ لم يتم العثور على مفتاح OpenAI')

print('DM : https://t.me/WHI3PER')
