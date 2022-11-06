import "./App.css";
import LandingPage from "./views/LandingPage";
import Nav from "./views/Nav";
import Margins from "./components/Margins";
import { useEffect, useState } from "react";
import ArticleData from "./views/ArticleData";
import { animateScroll as scroll } from "react-scroll";
function App() {
  const [data, setData] = useState({});
  const sendData = (d) => {
    setData(d);
  };

  const scrollTo = (pageId) => {
    setTimeout(() => {
      let page = document.getElementById(pageId);
      scroll.scrollTo(page.offsetTop);
    }, 100);
  };

  useEffect(() => {}, []);
  return (
    <div className="App">
      <Margins>
        <section id="landing" className="landing-section col-c-c">
          <LandingPage scrollTo={scrollTo} sendData={sendData} />
        </section>
      </Margins>
      {Object.entries(data).length !== 0 && (
        <section id="article" scrollTo={scrollTo} className="article-section">
          <Margins>
            <ArticleData data={data} />
          </Margins>
        </section>
      )}
    </div>
  );
}

export default App;
