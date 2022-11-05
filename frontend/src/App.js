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
    let page = document.getElementById(pageId);
    scroll.scrollTo(page.offsetTop);
  };

  useEffect(() => {
  }, []);
  return (
    <div className="App">
      <Margins>
        <section id="landing" className="landing-section col-c-c">
          <LandingPage scrollTo={scrollTo} sendData={sendData} />
        </section>
        <section id="article" scrollTo={scrollTo} className="article-section">
          <ArticleData data={data} />
        </section>
      </Margins>
    </div>
  );
}

export default App;
