import {React,useEffect,useState} from 'react'
import {Text,View,ScrollView,StyleSheet,FlatList,ActivityIndicator} from 'react-native'
import Home from './components/Home'
import colors from './fakedata'

export default function App(){
  const [isLoading,setLoading] = useState(true);

  const [data,setData]=useState([]);



  const renderItem=({item})=>(
    <Home color={item.color} hex={item.hex}/>
  )
  
  return(
    <View >
      <View style={styles.nav}>
          <Text style={styles.text}>Hello World</Text>
      </View>
      <ScrollView>
          <FlatList
            data={colors}
            renderItem={renderItem}
            keyExtractor={item=>item.color}
          
          />
      </ScrollView>
    </View>

  )
}


const styles=StyleSheet.create(
  {
    text:{
      color:"white",
      fontWeight:"bold",
    },
    nav:{
      padding:20,
      backgroundColor:"dodgerblue"
    }
  }
)