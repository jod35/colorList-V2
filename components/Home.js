import React from 'react';
import {Text,View} from 'react-native'

export default function Home({color,hex}){

    const textStyles={
        color:'white',
        backgroundColor:hex,
        padding:20,
        textTransform:'capitalize'
    }

    const text={
        color:'white'
    }

    return(
        <View style={textStyles}>
            <Text style={text}>{color}</Text>
        </View>
    )
}