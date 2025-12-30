import google.generativeai as genai

# YOUR KEY
API_KEY = "AIzaSyDiFAdpUCz3agJBTHHf9QFAUTH4F3guAzU"
genai.configure(api_key=API_KEY)

print("--- Checking Available Models for this Key ---")
try:
    # 1. List all models available to you
    found_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Found: {m.name}")
            found_models.append(m.name)

    # 2. Try to generate with the first available model
    if found_models:
        model_name = found_models[0].replace("models/", "") # Clean the name
        print(f"\n--- Testing Generation with '{model_name}' ---")
        
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello, do you work?")
        print(f"🎉 Success! Response: {response.text}")
    else:
        print("❌ No text generation models found for this API key.")

except Exception as e:
    print(f"\n❌ CRITICAL ERROR: {e}")