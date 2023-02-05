import React from 'react';
import { TextField } from '@mui/material';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
export default function Login() {
    const inputProps = {
        name: '',
        password: '',
    };
    const auth = () => {
        if ((inputProps.name === 'admin') && (inputProps.password === 'admin'))
        {
            console.log("logged in")
        }
    };

    return (<>
    <meta name="viewport" content="initial-scale=1, width=device-width" />
        <Box component="form" noValidate sx={{ p: 16, border: 0, borderColor: 'error.main', borderRadius: '16px' }}>
        <Stack spacing={2}>
            <TextField id="email" type="email" inputProps={inputProps.name} />
            <TextField id="spassword" type="password" inputProps={inputProps.password} />
            <Button onClick={auth()} variant="contained">Login</Button>
        </Stack>
        </Box>
    </>)
}
