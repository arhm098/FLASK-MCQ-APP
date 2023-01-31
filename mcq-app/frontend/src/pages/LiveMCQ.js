

import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import RadioGroup from '@mui/material/RadioGroup';
import Radio from '@mui/material/Radio';
import Box from '@mui/material/Box';
import { useEffect,useState } from 'react';
export default function LiveMCQ() {
  const [borderW,setBorderW] = useState(0);
  const [boderColor,setBorderColor] = useState("");
  // const []
  const [clicked, setClicked] = useState('option1');
  const [isClicked, setIsClicked] = useState(false)
  const [isRight,setIsRight] = useState(false)
  const handleChange = (event) => {
    setClicked(event.target.value);
  };
  const [data, setData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('http://localhost:3001/');
      const data = await response.json();
      setData(data);
    }
    fetchData();
  }, []);
    // const handleClick = () => {
    //   fetch('http://localhost:3001/', {
    //     method: 'POST',
    //     body: JSON.stringify({ message: value }),
    //     headers: {
    //       'Content-Type': 'application/json'
    //     }
    //   });
    // }
    const checkOption = () => {
        if (clicked === data.MCQ[5])
        {
          console.log("right click")
          setIsRight(true)
        }
        else
        {
          console.log("ghalat click")
          setIsRight(false)
        }
        setIsClicked(true)
    }
    const handleBorders =  () => {
      if (isClicked)
      { 
        setBorderW(5)
        if(isRight)
        {

        }
      }
      else
      {
        setBorderW(0)
      }
    }
      return (
        <>
          <meta name="viewport" content="initial-scale=1, width=device-width" />
          <Box component="form" noValidate sx={{ p: 16, border: 0, borderColor: 'error.main',borderRadius: '16px' }}>
            <Typography component="h1" variant="h5">
              {data? data.MCQ[0] : ""}
            </Typography>
            <RadioGroup
              aria-labelledby="demo-radio-buttons-group-label"
              defaultValue="female"
              name="radio-buttons-group" 
              value={clicked}  onChange={handleChange}
            >
              {isClicked ? (<><FormControlLabel value='1' control={<Radio />} disabled  label={data? data.MCQ[1]: ""} />
              <FormControlLabel  value='2' control={<Radio />} disabled   label={data? data.MCQ[2]: ""} />
              <FormControlLabel  value='3' control={<Radio />} disabled  label={data? data.MCQ[3]: ""} />
              <FormControlLabel value='4' control={<Radio />}  disabled label={data? data.MCQ[4]: ""} />
              {isRight ? (<><Button variant="contained" color="success" onClick={checkOption}>Submit</Button></>) : (<><Button variant="contained" color="error" onClick={checkOption}>Submit</Button></>)}
              </>) : (<>
              <FormControlLabel value='1' control={<Radio />}   label={data? data.MCQ[1]: ""} />
              <FormControlLabel  value='2' control={<Radio />}   label={data? data.MCQ[2]: ""} />
              <FormControlLabel  value='3' control={<Radio />}   label={data? data.MCQ[3]: ""} />
              <FormControlLabel value='4' control={<Radio />}   label={data? data.MCQ[4]: ""} />
              <Button variant="contained" onClick={checkOption}>Submit</Button></>)}
            </RadioGroup>
            </Box>
            <Box component="form" noValidate sx={{ px: 16 }}>
            {isClicked ? (
              <>
            <Typography component="h1" variant="h5">
              You clicked: {data? data.MCQ[clicked]: ""}
            </Typography>
              <Typography component="h1" variant="h5">
              Right Option :  {data? data.MCQ[data? data.MCQ[5]: ""]: ""}
              </Typography></>) :
               (<></>)
               }
          </Box>
        </>
      );

}
