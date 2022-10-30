import React, {useState} from "react";
import Form from "./Form";
import Results from "./Results";
import Image from "next/image";
import logo from "../public/brandykitt.png";

const BrandyKitt: React.FC = () => {
  const CHARACTER_LIMIT: number = 32;
  const ENDPOINT: string =
    "https://ck3xvhr72j.execute-api.us-east-1.amazonaws.com/prod/generate_snippet_keywords";
  const [prompt, setPrompt] = useState("");
  const [snippet, setSnippet] = useState("");
  const [keywords, setKeywords] = useState<string[]>([]);
  const [hasResult, setHasResult] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const onSubmit = () => {
    setIsLoading(true);
    fetch(`${ENDPOINT}?prompt=${prompt}`)
      .then((res) => res.json())
      .then(onResult);
  };

  const onResult = (data: any) => {
    setSnippet(data.snippet);
    setKeywords(data.keywords);
    setHasResult(true);
    setIsLoading(false);
  };

  const onReset = () => {
    setPrompt("");
    setHasResult(false);
    setIsLoading(false);
  };

  let displayedElement = null;

  if (hasResult) {
    displayedElement = (
      <Results
        snippet={snippet}
        keywords={keywords}
        onBack={onReset}
        prompt={prompt}
      />
    );
  } else {
    displayedElement = (
      <Form
        prompt={prompt}
        setPrompt={setPrompt}
        onSubmit={onSubmit}
        isLoading={isLoading}
        characterLimit={CHARACTER_LIMIT}
      />
    );
  }

  const gradientTextStyle =
    "text-white text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-blue-500 font-normal  w-fit mx-auto";

  return (
    <div className="h-screen flex">
      <div className="max-w-md m-auto p-2">
        <div className="bg-[#F3F4F6] p-6 rounded-md text-white">
          <div className="text-center my-6">
            <Image src={logo} width={65} height={65} alt="brandykitt logo" className="mx-auto" />
            <h1 className={gradientTextStyle + " text-3xl"}>
              BrandyKitt
            </h1>
            <div className={gradientTextStyle}>Your AI branding assistant</div>
          </div>

          {displayedElement}
        </div>
      </div>
    </div>
  );
};

export default BrandyKitt;