//_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/.
// 			VisualNovelToolkit		     /_/_/_/_/_/_/_/_/_/.
// Copyright ©2013 - Sol-tribe.	/_/_/_/_/_/_/_/_/_/.
//_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/.
using UnityEngine;
using System.Collections;

/// <summary>
/// Show GUI text_ level name at the top of left corner.
/// </summary>
public class GUIText_LevelName : MonoBehaviour {

	// Use this for initialization
	void Start () {
		if( GetComponent<GUIText>() != null ){	
			SetCurrentLevelName();
		}
	}
	
	void Update(){
		if( GetComponent<GUIText>() != null ){	
			if( string.IsNullOrEmpty( GetComponent<GUIText>().text ) || GetComponent<GUIText>().text != Application.loadedLevelName  ){	
				SetCurrentLevelName();
			}
		}
	}
	
	void SetCurrentLevelName( ){
		GetComponent<GUIText>().text = Application.loadedLevelName;			
	}
}
