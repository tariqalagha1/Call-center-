import os
from web_interface_rtl.app_arabic import create_app

def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        'uploads',
        'domains/clinic/prompts',
        'domains/clinic/sample_data',
        'domains/restaurant/prompts', 
        'domains/restaurant/sample_data',
        'domains/school/prompts',
        'domains/school/sample_data',
        'domains/office/prompts',
        'domains/office/sample_data',
        'web_interface_rtl/static/css',
        'web_interface_rtl/static/js'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
def check_env_variables():
    """Check if required environment variables are set"""
    required_vars = ['GROQ_API_KEY', 'DEEPGRAM_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"⚠️  Warning: Missing environment variables: {', '.join(missing_vars)}")
        print("Please set these in your .env file before running the application.")
        return False
    return True

if __name__ == '__main__':
    print("🚀 Starting Arabic RTL Call Center System...")
    
    # Create directories
    create_directories()
    print("✅ Project directories created")
    
    # Check environment variables
    env_ok = check_env_variables()
    
    # Create and run the app
    app = create_app()
    
    if env_ok:
        print("🌐 Starting server at http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("❌ Please configure your .env file first")