import React from 'react';

const HeroHome = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <header className="flex items-center justify-between bg-purple-400 p-4 rounded-lg">
        <div className="text-white font-bold text-xl">CURE CHAT</div>
        <input 
          type="text" 
          placeholder="Search Here" 
          className="bg-gray-200 rounded-full px-4 py-2 text-sm w-1/3" 
        />
        <img 
          src="src\assets\chatbot.png" 
          alt="Robot" 
          className="w-28 h-auto rounded-full"
        />
      </header>

      <nav className="flex justify-center space-x-8 bg-purple-300 py-2 mt-4 rounded-lg">
        {['Home', 'For You', 'Vaccines', 'Vitamin D', 'Arthritis'].map((item, index) => (
          <a key={index} href="#" className="text-white text-lg font-semibold">
            {item}
          </a>
        ))}
      </nav>
      <div className="flex mt-6 space-x-6">
        <div className="flex-1 bg-white p-4 rounded-lg shadow-lg">
          <div className="flex space-x-4 mb-6">
            <img src="src\assets\vaccine.jpg" alt="Vaccine" className="w-48 h-32 rounded-lg" />
            <div>
              <h2 className="text-lg font-semibold">"The Truth About Vaccines: Busting Myths and Misconceptions About Immunization"</h2>
              <p className="text-gray-600 mt-2">Vaccine safety concerns, from autism to infertility, persist despite overwhelming scientific evidence...</p>
              <button className="bg-purple-400 text-white px-4 py-2 rounded-lg mt-4">Read More</button>
            </div>
          </div>
          <hr />
          <div className="flex space-x-4 mt-6">
            <img src="src\assets\vitamin d.jpg" alt="Vitamin D" className="w-48 h-32 rounded-lg" />
            <div>
              <h2 className="text-lg font-semibold">"Debunking the Vitamin D Myth: What You Really Need to Know About Sun Exposure and Supplements"</h2>
              <p className="text-gray-600 mt-2">Many assume more vitamin D means stronger bones, but excessive supplementation can be harmful...</p>
              <button className="bg-purple-400 text-white px-4 py-2 rounded-lg mt-4">Read More</button>
            </div>
          </div>
        </div>
        <aside className="w-1/3 bg-white p-4 rounded-lg shadow-lg">
          <h3 className="text-xl font-bold mb-4">Top Picks</h3>
          <ul className="space-y-4">
            {[
              'The 8-Glasses-a-Day Rule: Debunking the Hydration Myth',
              'The Cold Weather Cold Myth: Why Temperature Doesn’t Cause Colds',
              'Detox Diets Exposed: Separating Cleansing Myths',
              'Cracking the Cholesterol Code: Busting Myths About Heart Health',
              'Are Antibiotics a Cure-All? Myth Busting Resistance',
              'Carbs and Weight Gain: Low-Carb Diet Myths'
            ].map((pick, index) => (
              <li key={index} className="border-b pb-2">
                <a href="#" className="text-gray-700 hover:underline">
                  {pick}
                </a>
              </li>
            ))}
          </ul>
        </aside>
      </div>
    </div>
  );
}

export default HeroHome;
