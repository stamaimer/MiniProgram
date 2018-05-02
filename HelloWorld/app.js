App({

  /**
   * 当小程序初始化完成时，会触发 onLaunch（全局只触发一次）
   */
  onLaunch: function () {
    
    let that = this;
     
     that.checkLoginStatus();
  },

  checkLoginStatus: function () {

    let that = this;
    let loginFlag = wx.getStorageSync('loginFlag');

    if (loginFlag) {

      wx.checkSession({
        
        success: function () {
           
          let userInfo = wx.getStorageInfoSync('userInfo');

          if (userInfo) {

            that.gloablData.userInfo = JSON.parse(userInfo);

          } else {

            that.showInfo('缓存信息失效');

            console.error('缓存信息失效');

          }
        },

        fail: function() {

          that.login()

        }

      });  

    } else {

      that.login()

    }
  },

  login: function () {

    let that = this;

    wx.login({
      
      success: function (loginRes) {

        if (loginRes.code) {

          wx.getUserInfo({
            
            withCredentials: true,

            success: function (infoRes) {

              console.log(infoRes)

              wx.request({

                url: 'http://139.199.167.51/login',

                data: {
                  code: loginRes.code,
                  rawData: infoRes.rawData,
                  signature: infoRes.signature,
                  encryptedData: infoRes.encryptedData,
                  iv: infoRes.iv
                },

                success: function (res) {

                  console.log('login success');

                  console.log(res);

                  res = res.data

                  if (res.result == 0) {



                  }

                },

                fail: function (error) {
                   
                }

              })

            }

          })  

        }

      }

    })

  },

  /**
   * 当小程序启动，或从后台进入前台显示，会触发 onShow
   */
  onShow: function (options) {
    
  },

  /**
   * 当小程序从前台进入后台，会触发 onHide
   */
  onHide: function () {
    
  },

  /**
   * 当小程序发生脚本错误，或者 api 调用失败时，会触发 onError 并带上错误信息
   */
  onError: function (msg) {
    
  }
})
